from django.db import models
from master.models import Basemodel,Technology
from master.utils.TA_UNIQUE.date_time import CURRENT_DATETIME
from master.utils.TA_UNIQUE.filename import unique_filename
from master.utils.TA_UNIQUE.unique_id import generate_uniq_id

from employee.constants.gender import CHOICH_GENDER
from .constants.coursestatus import COURSE_STATUS
from.constants.payment import PAYMENT_CHOICE

from decimal import Decimal

from django.core.exceptions import ValidationError
# from employee.models import Technology

# # Create your models here.

class Student(Basemodel):
    student_id = models.CharField(primary_key=True, blank=True, max_length=255)
    first_name = models.CharField(max_length=100,blank=False, null=False)
    last_name = models.CharField(max_length=100,blank=False, null=False)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    password = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f"{self.first_name}_{self.last_name}"
    
    def save(self,*args, **kwargs):
        month = CURRENT_DATETIME.month
        year =CURRENT_DATETIME.year
        PREFIX = 'STU'+month+year+'T'
        if not self.pk:
            last_student = Student.objects.order_by("-created_at").first()
            if last_student:
                last_numeric_part = int(last_student.student_id[len(PREFIX):])
                new_numeric_part = last_numeric_part +1
                new_id = f"{PREFIX}{new_numeric_part:04}"
            else:
                new_id = f"{PREFIX}0001"

            self.student_id = new_id
            self.password = self.mobile
        super(Student,self).save(*args, **kwargs)

class StudentProfile(Basemodel):
    DIR_NAME = 'student_profiles'
    SUFFIX_WORD = 'std_profile' 
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=unique_filename,blank=True)
    gender = models.CharField(choices=CHOICH_GENDER, max_length=20, blank=False)
    date_of_birth = models.DateField(blank=False)
    
    def __str__(self):
        return f"{self.student_id.first_name}"

    
class StudentAddress(Basemodel):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    address = models.CharField(max_length=225,blank=False)
    country = models.CharField(max_length=225,blank=False)
    state = models.CharField(max_length=225,blank=False)
    city = models.CharField(max_length=225,blank=False)
    pincode = models.CharField(max_length=225,blank=False)

class StudentCourse(Basemodel):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    technology_id = models.ForeignKey(Technology,on_delete=models.CASCADE)
    batch_start_date = models.DateField()
    batch_end_date = models.DateField()
    batch_status = models.CharField(choices=COURSE_STATUS,blank=False,max_length=20)

class StudentPayment(Basemodel):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    technology_id = models.ForeignKey(Technology,on_delete=models.CASCADE)
    total_fees = models.DecimalField(max_digits=10, default=Decimal('0.00'), decimal_places=2)
    remaining_fees = models.DecimalField(max_digits=10, default=Decimal('0.00'), decimal_places=2)
    paid_fees = models.DecimalField(max_digits=10, default=Decimal('0.00'), decimal_places=2)
    status = models.CharField(choices=PAYMENT_CHOICE, default='I', max_length=10)

    class Meta:
        unique_together = ("student_id","technology_id")

    def save(self,*args, **kwargs):

        self.total_fees = self.technology_id.fees
        self.remaining_fees = self.total_fees- self.paid_fees

        super(StudentPayment,self).save(*args, **kwargs)
    
class StudentPaymentEntry(Basemodel):
    DIR_NAME = 'Student_fees'
    SUFFIX_WORD = 'studentfees'
    payment_id = models.CharField(primary_key=True,max_length=255,blank=True)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    proof = models.ImageField(upload_to=unique_filename)
    paid_date = models.DateField()
    installment = models.DecimalField(max_digits=10,default=Decimal('0.00'),decimal_places=2)

    def save(self,*args, **kwargs):
        if not self.pk:
            self.payment_id = generate_uniq_id(self)
            try:
                student_fees_account = StudentPayment.objects.get(student_id_id = self.student_id_id)
            except StudentPayment.DoesNotExist:
                raise ValidationError("data not found")
            if self.installment != 0:
                if self.installment <= student_fees_account.remaining_fees:
                    student_fees_account.remaining_fees=student_fees_account.remaining_fees-self.installment
                    student_fees_account.paid_fees = student_fees_account.paid_fees + self.installment

                    if student_fees_account.remaining_fees != 0:
                        student_fees_account.status = "P"
                    else:
                        student_fees_account.status = "C"
                    student_fees_account.save()
                else:
                    raise ValidationError("Payment installment must be less than remaining fees")
            else:
                raise ValidationError("Payment installment must be greater than 0")
        super().save(*args,**kwargs)
