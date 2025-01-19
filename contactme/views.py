# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from contactme.models import contactmemodel

# Create your views here.
def contactform(request):
    param={'title':'contactme'}
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        name=fname+" "+lname
        email=request.POST.get("email")
        contactnumber=request.POST.get("contactnumber")
        designation=request.POST.get("designation")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        contactdata=contactmemodel(email_model=email, name_model=name, subject_model=subject, message_model=message, contactnumber_model=contactnumber, designation_model=designation)
        contactdata.save()
        return redirect(thankyou)
    return render(request, "contactme.html",param)

def thankyou(request):
    param={'title':'Thank You'}    
    return render(request, "thankyou.html",param)
