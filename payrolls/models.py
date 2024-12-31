from django.db import models

from accounts.models import User

class Payroll(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    tax_deduction = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def net_salary(self):
        return self.base_salary - self.tax_deduction

    def __str__(self):
        return f"{self.user.username} - {self.base_salary}"