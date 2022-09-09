from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "user_example/index.html")

@login_required
def special(request):
    return render(request, "user_example/special.html")

def register(request):
    form= UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")
    
    context = {
        'form': form
    }
    return render(request, "user_example/register.html", context)