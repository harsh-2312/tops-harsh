from django.contrib import admin

from .models import Employee,Batch,AssignBatch,EmployeeProfile
from .models import Role


# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeProfile)
admin.site.register(Role)
admin.site.register(Batch)
admin.site.register(AssignBatch)
