from django.db import models
from users.models import User


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('done', 'Done')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Answer(models.Model):

    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.answer
