from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages
from core import forms


def login_user(request):
    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.WARNING,
            f"Du bist bereits als {request.user.username} angemeldet.",
        )
        return redirect(reverse("home"))
    form = forms.PasswordForm()
    password_correct = request.session.get("password_correct", False)
    if request.method == "POST":
        if not password_correct:
            # if the password is not correct yet
            form = forms.PasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data["password"]
                if password == settings.PASSWORD:
                    request.session["password_correct"] = True
                    password_correct = True
                else:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        f"Das Passwort war leider falsch!",
                    )
        else:
            form = forms.UsernameForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                user, created = User.objects.get_or_create(username=username)
                if created:
                    user.set_password(username)
                    user.save()
                if user is not None:
                    login(request, user)
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        f"Erfolgreich als {request.user.username} angemeldet.",
                    )
                    return redirect(reverse("home"))

    return render(
        request, "login.html", {"form": form, "password_correct": password_correct}
    )
