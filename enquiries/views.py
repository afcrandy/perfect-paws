from django.conf import settings
from django.shortcuts import render


# Create your views here.
def contact_page(request):
    return render(
        request,
        'enquiries/contact.html',
        {'GOOGLE_MAPS_KEY': settings.GOOGLE_MAPS_API_KEY},
    )
