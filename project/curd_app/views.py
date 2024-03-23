from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import CarForm
from .models import Car


@login_required(login_url="login_url")
def car_view(request):
    template_name = "curd_app/car_info.html"
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_info(request):
    template_name = "curd_app/show_info.html"
    obj = Car.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = Car.objects.get(id=pk)
    form = CarForm(instance=obj)
    if request.method == "POST":
        form = CarForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_urls")
    template_name = 'curd_app/car_info.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_view(request, pk):
    obj = Car.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, "curd_app/confirm.html")
