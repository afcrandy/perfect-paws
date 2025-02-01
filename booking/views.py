from django.shortcuts import render


# Create your views here.
def services_info(request):
    return render(
        request,
        'booking/services_info.html',
    )

def make_booking(request):
    return render(
        request,
        'booking/booking_form.html',
    )
