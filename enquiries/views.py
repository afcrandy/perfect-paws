from django.conf import settings
from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import EnquiryForm


# Create your views here.
def contact_page(request):
    """
    Renders the contact page and handles submission of the enquiry form. If form
    submission is successful, a message is displayed to the user.
    
    **Context:**
        ``GOOGLE_MAPS_KEY``
            The Google Maps API key for displaying the map.
        ``enquiry_form``
            An instance of :form:`enquiries.EnquiryForm` used for submitting an enquiry.
    
    **Template:**
        :template:`enquiries/contact.html`
    """
    if request.method == "POST":
        enquiry_form = EnquiryForm(data=request.POST)
        if enquiry_form.is_valid():
            enquiry = enquiry_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your enquiry has been successfully sent"
            )
        return HttpResponseRedirect(reverse('contact'))
    
    enquiry_form = EnquiryForm()
    
    return render(
        request,
        'enquiries/contact.html',
        {
            'GOOGLE_MAPS_KEY': settings.GOOGLE_MAPS_API_KEY,
            'enquiry_form': enquiry_form,
        },
    )
