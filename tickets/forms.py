from django.forms import ModelForm, forms
from .models import Ticket, Answer


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['description', 'message']
        labels = {'description': 'Тема', 'message': 'Проблема'}




    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form__field_1'})
        self.fields['message'].widget.attrs.update({'class': 'form__field_1'})




class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['ticket_id', 'answer']

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)


class UpdateForm(ModelForm):
    model = Ticket
    fields = ['description', 'message']
