from django.contrib import admin

# Register your models here.

from .models import Role
from .models import society_member,SocietyWatchmen,notice_board,Event,visitor,charman

admin.site.register(Role)
admin.site.register(charman)
admin.site.register(society_member)
admin.site.register(SocietyWatchmen)
admin.site.register(notice_board)
admin.site.register(Event)
admin.site.register(visitor)
