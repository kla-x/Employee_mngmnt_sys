from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 

    path('logout/', views.user_logout, name='logout'),
]