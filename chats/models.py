from django.db import models

from accounts.models import User
from django.utils import timezone

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:20]}..."

class CommunityMessage(Message):
    pass

class DepartmentMessage(Message):
    pass

class Notification(Message):
    pass