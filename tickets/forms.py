from django.forms import ModelForm, forms
from .models import Ticket, Answer, Feedback


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
        labels = {'ticket_id': 'Заявка', 'answer': 'Ответ'}

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['ticket_id'].widget.attrs.update({'class': 'ticket_id'})


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['answer_id', 'feedback']
        labels = {'answer_id': 'Ответ поддержки', 'feedback': 'Комментарий'}

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
