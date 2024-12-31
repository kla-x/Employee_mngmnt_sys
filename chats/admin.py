from django.contrib import admin

# Register your models here.
from .models import CommunityMessage, DepartmentMessage, Notification

admin.site.register(CommunityMessage)
admin.site.register(DepartmentMessage)
admin.site.register(Notification)