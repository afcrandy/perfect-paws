from django.urls import path
from . import views


urlpatterns = [
    path('', views.perfect_paws_home, name='home'),
]
