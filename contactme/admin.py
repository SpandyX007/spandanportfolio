from django.contrib import admin
from .models import contactmemodel
# Register your models here.
class admincontactme(admin.ModelAdmin):
    list_display=("name_model","email_model","contactnumber_model","designation_model","subject_model","message_model")

admin.site.register(contactmemodel,admincontactme)