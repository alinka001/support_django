
from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('all/', views.tickets, name='tickets-all'),
    path('one/<str:pk>/', views.ticket, name='ticket'),
    path('create/', views.createTicket, name='create-ticket'),
    path('update/<str:pk>/', views.updateTicket, name='update-ticket'),
]
