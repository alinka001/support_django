from django.forms import ModelForm
from .models import Ticket, Answer


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['description', 'message']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
