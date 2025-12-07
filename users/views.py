import os

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from dotenv import load_dotenv

load_dotenv()


class RegisterView(CreateView):
    template_name = 'users/reg.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product-list-view')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать на наш сайт"
        message = "Спасибо что зарегистрировались"
        from_email = os.getenv('from_email')
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)