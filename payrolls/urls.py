from django.urls import path
from . import views
from django.views.defaults import page_not_found
from django.conf.urls import handler404

urlpatterns = [
    path('', views.payroll_view, name='payroll'),
    path( 'not_exist/', views.doesnt_exist, name='not_exist')
]

handler404 = 'payrolls.views.PagenotFound404'