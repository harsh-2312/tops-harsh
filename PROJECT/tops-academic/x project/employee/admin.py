from django.contrib import admin

from .models import Employee
from .models import Role
from .models import Student

# Register your models here.

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Student)
