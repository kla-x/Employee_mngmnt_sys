from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('community/', views.community_chat, name='community_chat'),
    path('department/', views.department_chat, name='department_chat'),
    path('notifications/', views.notifications_board, name='notifications_board'),
]