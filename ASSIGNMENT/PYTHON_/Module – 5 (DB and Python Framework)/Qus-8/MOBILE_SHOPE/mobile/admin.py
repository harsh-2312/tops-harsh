from django.contrib import admin

from .models import Brand,ProductCategory,singupdata,role

# Register your models here.

admin.site.register(singupdata)
admin.site.register(role)
admin.site.register(ProductCategory)
admin.site.register(Brand)


