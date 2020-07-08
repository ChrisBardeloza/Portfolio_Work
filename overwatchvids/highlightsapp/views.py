from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def highlights_view(request):
    return render(request, "highlights.html",{}) 

def hero_view(request):
    return render(request, "hero.html",{})

def useraccount_view(request):
    return render(request, "sign_in.html",{})