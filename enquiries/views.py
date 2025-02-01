from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .forms import EnquiryForm


# Create your views here.
def contact_page(request):
    if request.method == "POST":
        enquiry_form = EnquiryForm(data=request.POST)
        if enquiry_form.is_valid():
            enquiry = enquiry_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your enquiry has been successfully sent"
            )
    
    enquiry_form = EnquiryForm()
    
    return render(
        request,
        'enquiries/contact.html',
        {
            'GOOGLE_MAPS_KEY': settings.GOOGLE_MAPS_API_KEY,
            'enquiry_form': enquiry_form,
        },
    )
