from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userextend.models import UserExtend


class UserExtendCreateView(CreateView):
    template_name = "userextend/creaza_user.html"
    model = UserExtend
    # success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            user = form.save(commit=False)
            text_message = f"Your username is {user.username} and your password is {form.cleaned_data['password1']}"
            send_mail(subject="Create a new account", message=text_message, from_email=EMAIL_HOST_USER, recipient_list=[user.email])
            user.save()
            return redirect('login')


            # Pentru a va trimite un email cu username si parola este hash
            # user = form.save(commit=False)
            # text_message = f"Your username is{user.username} and your password {user.password}"
            # send_mail(subject="Create a new account", message=text_message, from_email=EMAIL_HOST_USER, recipient_list=[user.email])
            # user.save()
            # return redirect('login')