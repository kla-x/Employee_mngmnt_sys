from django.db import models

# Create your models here.

from accounts.models import User
from django.utils import timezone

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)  
    def __str__(self):
        return f"{self.user.username} - {self.date}"