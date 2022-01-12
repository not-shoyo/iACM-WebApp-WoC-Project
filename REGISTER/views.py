from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print("this")
        if form.is_valid():
            form.save()
            print("yay")
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "REGISTER/register.html", {
        "form" : form,  
    })