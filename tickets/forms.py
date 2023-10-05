from django.forms import ModelForm
from .models import Ticket, Answer


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['author', 'description', 'message']

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['ticket_id', 'answer']

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)


class UpdateForm(ModelForm):
    model = Ticket
    fields = ['description', 'message']
