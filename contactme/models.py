from django.db import models

# Create your models here.
class contactmemodel(models.Model):
    name_model=models.CharField(max_length=150,null=False, blank=False)
    email_model=models.EmailField(max_length=254,null=False, blank=False)
    contactnumber_model=models.CharField(max_length=12,null=False, blank=False)
    designation_model=models.CharField(max_length=100,null=False, blank=False)
    subject_model=models.CharField(max_length=150,null=False, blank=False)
    message_model=models.CharField(max_length=500,null=False, blank=False)