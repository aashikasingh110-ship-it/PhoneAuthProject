from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        phone_number = request.POST["phone_number"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=phone_number,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid phone number or password.")

    return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "accounts/home.html")