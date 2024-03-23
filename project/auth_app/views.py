from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def signup_view(request):
    template_name = "auth_app/signup.html"
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    context = {"form": form}
    return render(request, template_name, context)


def login_view(request):
    template_name = "auth_app/login.html"
    if request.method == "POST":
        un = request.POST["un"]
        pw = request.POST["pw"]
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect("show_url")
        else:
            return HttpResponse("enter correct un and pw")
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect("login_url")
