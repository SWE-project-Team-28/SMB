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


class ProfilePageTestCase(TestCase):

    def test_user_sign_in(self):
        # Make a POST request to the sign in page with user details
        response = self.client.post('/profile', {
            'username': 'testuser',
            'email': 'testuser@iith.ac.in',
            'password1': 'testpass',
            'password2': 'testpass',
        })

        # Check if the user is redirected to the home page after successful sign in
        self.assertRedirects(response, '/profile')


    def test_ask_question(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/questions/new')

    def test_view_questions_button(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/questions')

    def test_update_profile(self):
        response = self.client.post('/profile/update', {'Username':'changed','Email':'changed@iith.ac.in','bio':'bio'})
        self.assertEqual(response.status_code, 302)
        
        # Refresh the user from the database
        self.user.refresh_from_db()
        
        # Check that the profile has been updated
        self.assertEqual(self.user.Username, 'changed')
        
