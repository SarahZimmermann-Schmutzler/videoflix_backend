from django.test import TestCase
from django.test import Client
import unittest
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.

class VideoTest(unittest.TestCase):
    def test_videopage(self):
        self.client = Client()        
        self.user = User.objects.create_user('test_user', password='test_user')        
        self.client.login(username='test_user', password='test_user')        
        
        response = self.client.get('/api/videos/')
        self.assertEqual(response.status_code, 200)
    
    def test_loginpage(self):
        response = self.client.get('admin/')
        self.assertEqual(response.status_code, 200)