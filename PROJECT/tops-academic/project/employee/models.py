from django.db import models
from master.models import Basemodel,Technology
from master.utils.TA_UNIQUE.password import generate_password
from master.utils.TA_UNIQUE.filename import unique_filename
from .constants.gender import CHOICH_GENDER

import os
from django.core.mail import send_mail

from student.models import Student


# # Create your models here.


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


class EmployeeProfile(Basemodel):
    DIR_NAME = "employee_profile"
    SUFFIX_WORD = 'empProfile'
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=unique_filename,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    gender = models.CharField(choices=CHOICH_GENDER,max_length=20,blank=True,null=True)
            

class Batch(Basemodel):
    PRIFIX = "BATCH"
    batch_id = models.CharField(primary_key=True,blank=True,max_length=225)
    batch_name= models.CharField(max_length=255)
    faculty_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    technology_id = models.ForeignKey(Technology,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.batch_name
    
    def save(self ,*args, **kwargs):
        if not self.pk:
            last_batch = Batch.objects.order_by("-created_at").first()
            if last_batch:
                last_numeric_part = int(last_batch.batch_id[len(self.PRIFIX):])
                new_numeric_part = last_numeric_part + 1
                new_id = f"{self.PRIFIX}{new_numeric_part:04}"
            else:
                new_id = f"{self.PRIFIX}001"

            self.batch_id = new_id
        super(Batch , self).save(*args, **kwargs)

class AssignBatch(Basemodel):
    batch_id = models.ForeignKey(Batch, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.batch_id.batch_id}_{self.student_id.student_id}_{self.student_id.first_name}"