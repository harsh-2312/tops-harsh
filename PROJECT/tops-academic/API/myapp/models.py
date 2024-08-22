from django.db import models
from django.utils import timezone

# Create your models here.

class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self,*args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        super(Basemodel,self).save(*args, **kwargs)


class Globalnote(Basemodel):
    student_id = models.CharField(max_length=225)
    comment = models.CharField(max_length=225)

