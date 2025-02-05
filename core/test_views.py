from django.urls import reverse
from django.test import TestCase


class TestCoreViews(TestCase):

    def test_home_page_renders_correctly(self):
        """Test that the home page loads correctly."""
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200, msg="Home page did not load correctly.")
        self.assertTemplateUsed(response, 'core/home.html')
