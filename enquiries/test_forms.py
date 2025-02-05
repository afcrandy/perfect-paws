from django.test import TestCase
from enquiries.forms import EnquiryForm


class TestEnquiryForm(TestCase):

    def setUp(self):
        """Set up initial data for enquiry tests."""
        self.valid_data = {
            'enquirer_name': 'John Doe',
            'enquirer_email': 'johndoe@example.com',
            'enquirer_phone': '07123 456 789',
            'content': 'I would like to know more about your services.'
        }

    def test_form_is_valid(self):
        """
        Test for all fields
        """
        form = EnquiryForm(data=self.valid_data)
        self.assertTrue(form.is_valid(), msg="Enquiry form is not valid")

    def test_name_is_required(self):
        """
        Test name field is required.
        """
        form = EnquiryForm(data=self.valid_data.copy())
        form.data['enquirer_name'] = ''
        self.assertFalse(form.is_valid(), msg="Name was not provided, but the form is valid")

    def test_email_is_required(self):
        """
        Test email field is required.
        """
        form = EnquiryForm(data=self.valid_data.copy())
        form.data['enquirer_email'] = ''
        self.assertFalse(form.is_valid(), msg="Email was not provided, but the form is valid")

    def test_phone_is_required(self):
        """
        Test phone field is required.
        """
        form = EnquiryForm(data=self.valid_data.copy())
        form.data['enquirer_phone'] = ''
        self.assertFalse(form.is_valid(), msg="Phone was not provided, but the form is valid")

    def test_content_is_required(self):
        """
        Test content field is required.
        """
        form = EnquiryForm(data=self.valid_data.copy())
        form.data['content'] = ''
        self.assertFalse(form.is_valid(), msg="Content was not provided, but the form is valid")

    def test_email_is_valid(self):
        """
        Test email format
        """
        form = EnquiryForm(data=self.valid_data.copy())
        form.data['enquirer_email'] = 'invalidemail.com'
        self.assertFalse(form.is_valid(), msg="Invalid email format was accepted")
