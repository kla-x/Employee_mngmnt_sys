from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Attendance

User = get_user_model()

class AttendanceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            email='test@example.com'
        )

    def test_valid_attendance_marking(self):
        self.client.login(username='testuser', password='testpass')

        response = self.client.post('/attendances/', follow=True)

        self.assertEqual(response.status_code, 200)
        attendance = Attendance.objects.filter(user=self.user, date=timezone.now().date()).first()
        self.assertIsNotNone(attendance)
        self.assertTrue(attendance.status)