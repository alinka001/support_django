
from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('all/', views.tickets, name='tickets-all'),
    path('one/<str:pk>/', views.ticket, name='ticket'),
    path('create/', views.createTicket, name='new-ticket'),
    path('delete/<str:pk>', views.deleteTicket, name="delete-ticket"),
    path('update/<int:pk>/', views.updateTicket, name='update'),
    path('answer/', views.createAnswer, name='answer'),
]
