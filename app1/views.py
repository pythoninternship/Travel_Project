from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

# Create your views here.
def project(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"result.html",{'add':add,'sub':sub,'mul':mul,'div':div})
