import json
from itertools import groupby
from operator import itemgetter
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from .models import Service, Booking
from .forms import BookingForm, BookingDateTimeForm, BookingDogInfoForm


# Create your views here.
def services_info(request):
    """
    Renders the services information page.
    Pulls the active services from the database and renders their information

    **Context**
        ``services``
            The set of active :model:`booking.Service` records

    **Template:**
        :template:`booking/services_info.html`
    """
    services = Service.objects.filter(active=True).order_by('-duration')
    # force HTTPS requests for Cloudinary-based images
    for service in services:
        service.image.url_options.update({'secure':True})
    return render(
        request,
        'booking/services_info.html',
        {
            'services': services,
        }
    )

@login_required
def make_booking(request):
    """
    Renders the booking form and allows users to submit bookings

    Users must be logged in to view the page.

    **Context**
        ``services``
            The set of active :model:`booking.Service` records
        ``booking_form``
            An instance of :form:`booking.BookingForm`
        ``date_time_form``
            An instance of :form:`booking.BookingDateTimeForm`
        ``dog_info_form``
            An instance of :form:`booking.BookingDogInfoForm`

    **Template:**
        :template:`booking/booking_form.html`
    """
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.client = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                f"Your booking has been confirmed: for {booking.dog_name} on {booking.date.strftime('%d-%m-%y')} at {booking.time.strftime('%H:%M')}"
            )

            # build the content and context for the confirmation email
            email_context = {
                'booking': booking,
                'user': booking.client,
                'service_name': booking.service.name,
            }
            email_message = render_to_string(
                'emails/booking_confirmation_email.txt', email_context
            )
            send_mail(
                f"Booking Confirmation: {booking.dog_name}",
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [booking.client.email],
                fail_silently=False
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'There was an error confirming your booking. Please contact us if this persists'
            )
        return HttpResponseRedirect(reverse('home'))

    services = Service.objects.filter(active=True).order_by('-duration')
    # force HTTPS requests for Cloudinary-based images
    for service in services:
        service.image.url_options.update({'secure':True})
    booking_form = BookingForm()
    date_time_form = BookingDateTimeForm()
    dog_info_form = BookingDogInfoForm()

    return render(
        request,
        'booking/booking_form.html',
        {
            'services': services,
            'booking_form': booking_form,
            'date_time_form': date_time_form,
            'dog_info_form': dog_info_form,
        },
    )

def check_availability(request):
    """
    Handles AJAX requests from the services selector in the booking form

    Returns availability information for dates and times as JSON

    **Returns**
        ``unavailable_days``
            An array of dates that for the given type of service are fully booked
        ``used_slots``
            An associative array of { `date`: `[array of times already booked]` }
    """
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    t_date = date.today()

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)

            # parse the payload and retrieve booking records
            payload = data['payload']
            queryset = Booking.objects.filter(
                canceled=False,
                date__gt=t_date
            ).order_by('date')

            # determing the service type to compare against
            long = payload['slot'] == "long"
            if long:
                queryset = queryset.filter(service__duration__gt=60)
            else:
                queryset = queryset.filter(service__duration__lte=60)
            
            full_number = 4 if long else 7

            # calculate the number of bookings per day
            bookings_per_day = queryset.values('date', 'time')
            bookings_per_day = sorted(bookings_per_day, key=itemgetter('date'))
            bookings_per_day = {
                date: [booking['time'] for booking in group]
                for date, group in groupby(bookings_per_day, key=itemgetter('date'))
            }

            unavailable_days = [
                date.strftime('%Y-%m-%d') for date, times in bookings_per_day.items() if len(times) == full_number
            ]
            used_slots = {
                date.strftime('%Y-%m-%d'): [time.strftime("%H:%M") for time in times]
                for date, times in bookings_per_day.items() if len(times) < full_number
            }
            
            return JsonResponse({
                 'unavailable_days': unavailable_days,
                 'used_slots': used_slots
            })
        return JsonResponse({
             'status': 'it didnae work'
        }, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
