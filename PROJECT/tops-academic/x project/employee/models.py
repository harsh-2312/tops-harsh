from django.db import models
from master.models import Basemodel

from master.utils.TA_UNIQUE.password import generate_password

import os
from django.core.mail import send_mail

# Create your models here.


class Role(Basemodel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(Basemodel):
    PREFIX = 'EMP'
    employee_id = models.CharField(primary_key=True, blank=True, max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    mobile = models.CharField(max_length=50,  blank=False, null=False, unique=True)
    password = models.CharField(blank=True, max_length=255)
    is_active = models.BooleanField(default=True)   
    otp = models.CharField(default='123456', max_length=10)

    def __str__(self):
        return f'{self.employee_id}_{self.first_name}_{self.last_name}'

    def  save(self,*args, **kwargs):
        if not self.pk:
            last_employee = Employee.objects.order_by('-created_at').first()
            if last_employee:
                last_numeric_part = int(last_employee.employee_id[3:])
                new_numeric_part = last_numeric_part + 1
                new_id = f"{self.PREFIX}{new_numeric_part:04}"
            else:
                new_id = f"{self.PREFIX}0001"

            self.employee_id = new_id
            self.password = generate_password()


            subject = 'Your Login Credentials for Tops Technology Pvt. Ltd.'
            message = f"""
            Dear {self.first_name} {self.last_name},

            Welcome to Tops Technology Pvt. Ltd.! Your login credentials are as follows:

            Employee ID: {self.employee_id }
            Password: {self.password }
            Login your account: http://127.0.0.1:8000/employee/

            For security reasons, we recommend changing your password upon your first login. You can change your password by logging into your account and navigating to the settings or profile section.

            Please keep this information secure and do not share it with anyone. If you have any questions or need assistance, feel free to contact our support team.

            Best regards,
            Tops Technology Pvt. Ltd. Team
            """

            from_email = os.getenv('EMAIL_HOST_USER')
            recipient_list = [f'{self.email}']
            send_mail(subject, message, from_email, recipient_list)
        super(Employee, self).save(*args, **kwargs)




class Student(Basemodel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




        
            



