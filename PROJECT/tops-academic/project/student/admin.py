from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(StudentAddress)
admin.site.register(StudentCourse)
admin.site.register(StudentPayment)
admin.site.register(StudentPaymentEntry)
