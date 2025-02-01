from django.shortcuts import render
from .models import Service


# Create your views here.
def services_info(request):
    services = Service.objects.filter(active=True).order_by('-cost')
    return render(
        request,
        'booking/services_info.html',
        {
            'services': services,
        }
    )

def make_booking(request):
    return render(
        request,
        'booking/booking_form.html',
    )
