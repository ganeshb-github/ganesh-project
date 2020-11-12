from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    content ={
        'title':'Home'
    }
    return render(request,'frontend/pages/home/home.html')


def about(request):
    content={
        'title':'About'

    }
    return render(request,'frontent/pages/about/about.html')


def contact(request):
    content={
        'title':'contact'
    }
    return render(request,'frontend/pages/contact/contact.html')
