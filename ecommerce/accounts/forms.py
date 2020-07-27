from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'placeholder': 'Confirm password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
        }

class LoginForm():
    pass