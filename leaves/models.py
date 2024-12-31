from django.db import models

from django.db import models
from accounts.models import User

class LeaveRequest(models.Model):

    IS_APPROVED = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Declined', 'Declined'),
    )
    REASON = (
        ('Medical reasons', 'Medical reasons'),
        ('Vacation/holiday', 'Vacation/holiday'),
        ('Bereavement/funeral', 'Bereavement/funeral'),
        ('Maternity/paternity leave', 'Maternity/paternity leave'),
        ('Relocation/moving', 'Relocation/moving'),
        ('Wedding/planned event', 'Wedding/planned event'),
        ('Religious observance', 'Religious observance'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(default='Medical reasons', null=False,max_length=100, choices=REASON)
    is_approved = models.CharField(default='Pending', null=False,max_length=15, choices=IS_APPROVED)

    def __str__(self):
        return f"{self.user.username} - {self.start_date} to {self.end_date}"