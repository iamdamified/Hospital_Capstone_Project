from django.contrib import admin
from .models import Intro, Department, Patient, Doctor, Appointment

# Register your models here.

admin.site.register(Intro)
admin.site.register(Department)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)

