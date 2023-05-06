from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class UserSignInTestCase(TestCase):
    def test_user_sign_in(self):
        # Make a POST request to the sign in page with user details
        response = self.client.post('/', {
            'username': 'testuser',
            'email': 'testuser@iith.ac.in',
            'password1': 'testpass',
            'password2': 'testpass',
        })

        # Check if the user is redirected to the home page after successful sign in
        self.assertRedirects(response, '/')

        # Check if the user is created in the database
        #user_exists = User.objects.filter(username='testuser').exists()
        #self.assertTrue(user_exists)


