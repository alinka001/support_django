from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
