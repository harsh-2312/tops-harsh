from django.db import models
from django.utils import timezone
from master.utils.TA_UNIQUE.filename import unique_filename

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
    

class Technology(Basemodel):
    DIR_NAME = 'technology_logs'
    PRIFIX ='_Techlogo'
    SUFFIX_WORD =' Techlogo_'
    technology_id = models.CharField(primary_key=True,blank=True ,max_length=255)
    name = models.CharField(max_length=255 ,blank=False,null=False)
    logo = models.ImageField(upload_to=unique_filename,blank=True,null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.pk:
            last_technologe = Technology.objects.order_by("-created_at").first()
            if last_technologe:
                last_numeric = int(last_technologe.technology_id[len(self.PRIFIX)])
                new_numeric = last_numeric + 1
                new_id = f"{self.PRIFIX}{new_numeric:04}"
            else:
                new_id = f"{self.PRIFIX}001"
            self.technology_id = new_id
        
        super(Technology,self).save(*args, **kwargs)