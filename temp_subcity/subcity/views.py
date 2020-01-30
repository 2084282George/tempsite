from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'subcity/index.html')

def about(request):
    return render(request,'subcity/about.html')

def contact(request):
    return render(request,'subcity/contact.html')

def schedule(request):
    return render(request,'subcity/schedule.html')