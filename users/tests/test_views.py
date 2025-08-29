from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser

User = get_user_model()

class UserViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def setUp(self):
        self.client = Client()
        self.client.login(username='testuser', password='testpass123')

    def test_user_signup(self):
        data = {
            "username": "TestUserName",
            "password1": "TestPassword123!",
            "password2": "TestPassword123!",
        }
        client = Client()
        response = client.post(reverse("signup"), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(username='TestUserName').exists())
        self.assertTrue(CustomUser.objects.count(), 1)

    def test_user_signup_with_already_exists_username(self):
        data = {
            "username": CustomUser.objects.first().username,
            "password1": "TestPassword123!",
            "password2": "TestPassword123!",
        }
        client = Client()
        response = client.post(reverse("signup"), data=data)
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        login_data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        client = Client()
        response = client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('user-list'))


    def test_user_list_view_status_code(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)


    def test_user_list_view_no_access_status_code(self):
        response = Client().get(reverse('user-list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_user_detail_view_status_code(self):
        response = self.client.get(CustomUser.objects.first().get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_user_detail_view_no_access_status_code(self):
        response = Client().get(CustomUser.objects.first().get_absolute_url())
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)
