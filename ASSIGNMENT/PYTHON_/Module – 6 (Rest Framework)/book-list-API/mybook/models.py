from django.db import models
from django.utils import timezone

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at =timezone.now()

        super(BaseModel ,self).save(*args, **kwargs)

class Book(BaseModel):
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Isbn = models.CharField(max_length=255)
    Publisher = models.CharField(max_length=255)
