from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'image_user', 'country', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    pass 