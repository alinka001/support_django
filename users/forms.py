from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password', 'password2']


        def __init__(self, *args, **kwargs):
            super(CreateUserForm).__init__(*args, **kwargs)  # self

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})

