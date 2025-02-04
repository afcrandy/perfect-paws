from django.urls import path
from . import views


urlpatterns = [
    path('', views.services_info, name='services_info'),
    path('book/', views.make_booking, name='booking_form'),
    path('book/select-service/', views.check_availability, name='check_availability'),
]
