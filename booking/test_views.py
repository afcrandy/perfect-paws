from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from .models import Service, Booking
from datetime import datetime
import json

class TestBookingViews(TestCase):
    
    def setUp(self):
        """Set up necessary data for the tests."""
        # Create a test user
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

        # Create a sample active service
        self.service = Service.objects.create(
            name='Dog Walking',
            description='Walk your dog with a professional.',
            active=True,
            duration=30,
            cost=22.50,
        )

        self.services_info_url = reverse('services_info')
        self.make_booking_url = reverse('booking_form')
        self.check_availability_url = reverse('check_availability')

    def test_services_info(self):
        """Test the services info page."""
        response = self.client.get(self.services_info_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.service.name)
        self.assertTemplateUsed(response, 'booking/services_info.html')

    def test_make_booking_form_renders(self):
        """Test the booking form page renders properly."""
        response = self.client.get(self.make_booking_url)
        self.assertRedirects(response, '/accounts/login/?next=/services/book/')
        
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        
        response = self.client.get(self.make_booking_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_form.html')
        self.assertContains(response, 'Pick a service')

    def test_successful_booking_submission(self):
        """Test that a booking is created when valid data is submitted."""
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        
        booking_data = {
            'service': self.service.id,
            'client': self.user.id,
            'dog_name': 'Rex',
            'dog_breed': 'Labrador',
            'dog_size': 1,
            'date': datetime.today().date(),
            'time': datetime.strptime('10:00', '%H:%M').time(),
        }

        response = self.client.post(self.make_booking_url, booking_data)
        
        # Check if the booking is created
        booking = Booking.objects.first()
        self.assertIsNotNone(booking)
        self.assertEqual(booking.dog_name, 'Rex')

    def test_check_availability(self):
        """Test the availability check AJAX view."""
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        
        # Prepare POST data for the AJAX request
        post_data = {
            'payload': {
                'slot': 'long',
            }
        }

        response = self.client.post(
            self.check_availability_url,
            json.dumps(post_data),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        
        # Check if the response contains 'unavailable_days' and 'used_slots'
        self.assertIn('unavailable_days', response_data)
        self.assertIn('used_slots', response_data)

    def test_check_availability_invalid_request(self):
        """Test handling of invalid requests to the availability check view."""
        response = self.client.get(self.check_availability_url)
        self.assertEqual(response.status_code, 400)
