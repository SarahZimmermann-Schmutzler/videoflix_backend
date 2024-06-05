from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse


# Create your tests here.

class LoginViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')  # Passe den URL-Namen an, falls er anders lautet
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')

    def test_login_success(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
        self.assertIn('user_id', response.data)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'], 'test@example.com')

    def test_login_failure(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'wrongpassword'}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('token', response.data)
        self.assertNotIn('user_id', response.data)
        self.assertNotIn('email', response.data)

