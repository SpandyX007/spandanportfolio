from django.shortcuts import render
from django.http import HttpResponse
from contactme.models import contactmemodel

def mainhome(request):
    param={'title':"Spandy's Portfolio"}
    return render(request,'index1.html',param)