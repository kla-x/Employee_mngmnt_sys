from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    f_name = models.CharField(max_length=100, unique=False, null=True)  
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    phone_number = models.CharField(max_length=10, unique=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    bank_account_number  = models.CharField(max_length=12, unique=True,)
    is_approved = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    is_dep_lead = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set'
    )

    # Added related_name to remove clashing with auth.User.user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set'
    )