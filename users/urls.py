from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.user_profile, name='profile'),
    path('<int:id>/update_user/', views.user_update, name='update_user'),
    path('<int:id>/delete_user', views.user_delete, name='delete_user'),
]