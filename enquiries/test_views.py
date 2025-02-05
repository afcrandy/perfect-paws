from django.urls import reverse
from django.test import TestCase
from .models import Enquiry
from .forms import EnquiryForm


class TestEnquiriesViews(TestCase):

    def setUp(self):
        """Set up initial data for enquiry views tests."""
        # Create a sample enquiry record for testing
        self.enquiry_data = {
            'enquirer_name': 'John Doe',
            'enquirer_email': 'johndoe@example.com',
            'enquirer_phone': '1234567890',
            'content': 'I would like to know more about your services.'
        }
        self.enquiry = Enquiry.objects.create(**self.enquiry_data)

    def test_contact_page_renders_correctly(self):
        """
        Test that the contact page loads with the form.
        """
        response = self.client.get(reverse('contact'))

        self.assertEqual(response.status_code, 200, msg="Enquiry page did not load correctly.")
        self.assertIn(b'Send a message', response.content, msg="Enquiry form not present in the response.")
        self.assertIsInstance(response.context['enquiry_form'], EnquiryForm, msg="Form instance is incorrect in the context.")
    
    def test_enquiry_submission_success(self):
        """Test for submitting a valid enquiry."""
        post_data = {
            'enquirer_name': 'Jane Smith',
            'enquirer_email': 'janesmith@example.com',
            'enquirer_phone': '07123456789',
            'content': 'I want to ask about your Puppy Groom service.',
        }

        response = self.client.post(reverse('contact'), data=post_data)
        
        # Check for success status and response
        self.assertEqual(response.status_code, 302, msg="Response status code is not redirect as expected after submission.")
        
        # Check if the enquiry was actually saved in the database
        self.assertTrue(Enquiry.objects.filter(enquirer_email='janesmith@example.com').exists(), msg="Enquiry was not saved to the database.")
