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
            self.create_at=timezone.now()
        self.update_at=timezone.now()
        super(Basemodel,self).save(*args, **kwargs)
    
