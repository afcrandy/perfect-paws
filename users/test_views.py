from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages

class TestUserViews(TestCase):

    def setUp(self):
        """Set up a test user for login/logout tests."""
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '07123456789',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.login_url = reverse('account_login')
        self.logout_url = reverse('account_logout')
        self.profile_url = reverse('profile', args=[self.user.id])

    def test_user_registration(self):
        """Test user registration form works and redirects to login page."""
        registration_data = {
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }
        
        response = self.client.post(reverse('account_signup'), registration_data)
        
        # Ensure redirection to the login page after registration
        self.assertRedirects(response, reverse('home'))
        
        # Ensure the user is created
        user = get_user_model().objects.get(email='newuser@example.com')
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password('newpassword123'))
