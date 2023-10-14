from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from app.models import User
from app import forms


class LogInForm(forms.Form):
    __title__ = "Log in"
    email = forms.CharField("Email address", User.email)
    password = forms.PasswordField("Password")
    submit = forms.SubmitButton("Log me in")


class LogInView(View):
    def get(self, request, tr, path):
        form = LogInForm(request)
        return render(request, f"log-in.html", {f"form": form})

    def post(self, request, tr, path):
        form = LogInForm(request)
        if not form.is_valid:
            return render(request, f"log-in.html", {f"form": form})

        user = authenticate(request, username=form.email, password=form.password)
        if user is None:
            form.add_error(tr("Invalid email address or password."))
            return render(request, f"log-in.html", {f"form": form})

        language = request.session[f"language"]
        login(request, user)
        request.session[f"language"] = language

        if path.startswith(f"/"):
            return redirect(path)

        return redirect(f"account")


class LogOutView(View):
    def get(self, request, tr):
        language = request.session[f"language"]
        logout(request)
        request.session[f"language"] = language
        return render(request, f"log-out.html")
