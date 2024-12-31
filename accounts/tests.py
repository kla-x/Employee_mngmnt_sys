# accounts/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            is_approved=True,
            bank_account_number='12345678'
        )

    def test_login_view(self):
        # Test GET request
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_valid_login(self):
        # Test valid login
        login_data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(reverse('login'), data=login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('dashboard'))

    def test_invalid_login(self):
        # Test invalid login
        invalid_login_data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('login'), data=invalid_login_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_unapproved_user_login(self):
        unapproved_user = User.objects.create_user(
            username='unapproveduser',
            password='testpass',
            is_approved=False,
            bank_account_number='87654321'
        )
        login_data = {
            'username': 'unapproveduser',
            'password': 'testpass'
        }
        response = self.client.post(reverse('login'), data=login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/waiting_approval.html')