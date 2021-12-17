from django.http import HttpResponse
from django.shortcuts import render
from .models import place
# Create your views here.
def index(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})


# def addition(request):
#     a=int(request.GET['first number'])
#     b=int(request.GET['second number'])
#     add=a+b
#     mul=a*b
#     sub=a-b
#     div=a/b
#     return render(request,"about.html",{'result':add,'mul':mul,'sub':sub,'div':div})