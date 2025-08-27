from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()

class PhotoViewsTests(TestCase):

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
        self.upload_photo_url = reverse('photos:upload')

    def test_upload_photo_status_code(self):
        response = self.client.get(self.upload_photo_url)
        self.assertEqual(response.status_code, 200)

    def test_upload_photo_without_access_status_code(self):
        response = Client().get(self.upload_photo_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)
