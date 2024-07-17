from django.db import models
from django.utils import timezone

# Create your models here.

class Basemodel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self,*args, **kwargs):
        if not self.pk:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Basemodel,self).save(*args, **kwargs)