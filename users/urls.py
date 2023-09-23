from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.Users, name="users"),
    path('user/', views.UserSingle, name="user"),
]
