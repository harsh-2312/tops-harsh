from django.db import models
from master.models import Basemodel

from master.utils.TA_UNIQUE.password import generate_password
import os
from django.core.mail import send_mail

# Create your models here.

class Role(Basemodel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
class charman(Basemodel):
    PREFIX = 'CHA'
    charman_id =models.CharField(primary_key=True, blank=True,max_length=225)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225,unique=True)
    password = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.pk:
            last_charman = charman.objects.order_by("-created_at").first()
            if last_charman:
                last_numeric_part = int(last_charman.charman_id[3:])
                new_numeric_part = last_numeric_part + 1
                new_id = f"{self.PREFIX}{new_numeric_part:04}"
            else:
                new_id =f"{self.PREFIX}0001"
            
            self.charman_id =new_id
            self.password = generate_password()
        super(charman,self).save(*args, **kwargs)

class society_member(Basemodel):
    PREFIX = 'SOC'
    member_id = models.CharField(primary_key=True, blank=True,max_length=225)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    house_number = models.CharField(max_length=225, blank=False, null=False, unique=True)
    mobile_number = models.CharField(max_length=225, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=225,  blank=False, null=False, unique=True)
    password = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f'{self.member_id}_{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            last_member = society_member.objects.order_by("-created_at").first()
            if last_member:
                last_numeric_part = int(last_member.member_id[3:])
                new_numeric_part = last_numeric_part + 1
                new_id = f"{self.PREFIX}{new_numeric_part:04}"
            else:
                new_id = f'{self.PREFIX}0001'

            self.member_id = new_id
            self.password = generate_password()
        super(society_member,self).save(*args, **kwargs)

class SocietyWatchmen(Basemodel):
    PREFIX = "WAC"
    Watchmen_id = models.CharField(primary_key=True, blank=True,max_length=225)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    number = models.CharField(max_length=225, blank=False, null=False, unique=True)
    password = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f"{self.Watchmen_id}_{self.name}"
    
    def save(self,*args, **kwargs):
        if not self.pk:
            last_watchman = SocietyWatchmen.objects.order_by("-created_at").first()
            if last_watchman:
                last_numeric_part = int(last_watchman.Watchmen_id[3:])
                new_numeric_part = last_numeric_part + 1
                new_id = f"{self.PREFIX}{new_numeric_part:04}"
            else:
                new_id= F"{self.PREFIX}0001"

            self.Watchmen_id = new_id
            self.password = generate_password()
        super(SocietyWatchmen,self).save(*args, **kwargs)

class notice_board(Basemodel):
    title = models.CharField(max_length=225)
    img= models.ImageField(upload_to='logo/',blank=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.title}"

class Event(Basemodel):
    title = models.CharField(max_length=225)
    img= models.ImageField(upload_to='event/',blank=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.title}"
    
class visitor(Basemodel):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=225, blank=False, null=False, unique=True)
    visit_date = models.DateField()
    entry_time = models.TimeField()
    exit_time = models.TimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.name}"
    