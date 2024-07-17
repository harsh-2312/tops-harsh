from django.db import models
from master.models import Basemodel
from master.utils.TA_UNIQUE.password import password_get
import os

# Create your models here.
class Brand(Basemodel):
    brand_name = models.CharField(max_length=255)

    class Meta:
        unique_together = ['brand_name']
    
    def __str__(self):
        return self.brand_name

class ProductCategory(Basemodel):
    PRIFIX = 'PROD'
    product_id = models.CharField(primary_key=True, blank=True, max_length=255)
    brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=225 , blank=False)
    product_ram = models.CharField(max_length=225 , blank=False)
    image = models.ImageField(upload_to='logo/',blank=True)
    price = models.CharField(max_length=225 , blank=False)
    
    def __str__(self):
        return self.product_id
    
    def save(self,*args,**kwargs):
        if not self.pk:
            last_product = ProductCategory.objects.order_by('-created').first()
            if last_product:
                numeric_value = int(last_product.product_id[len(self.PRIFIX):])
                new_value = numeric_value + 1
                new_id = f"{self.PRIFIX}{new_value:04}"
            else:
                new_id = f"{self.PRIFIX}0001"
            
            self.product_id = new_id
        super(ProductCategory,self).save(*args,**kwargs)


class role(Basemodel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class singupdata(Basemodel):
    PRIFIX ='USR'
    user_id = models.CharField(primary_key=True, blank=True, max_length=255)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    mobile= models.CharField(max_length=10,blank=False, null=False, unique=True)
    password = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f'{self.user_id}_{self.name}'
    
    def save(self,*args, **kwargs):
        if not self.pk:
            lastuser= singupdata.objects.order_by('-created').first()
            if lastuser:
                last_num = int(lastuser.user_id[3:])
                new_num = last_num +1
                new_id = f"{self.PRIFIX}{new_num:04}"
            else:
                new_id =f"{self.PRIFIX}0001"

            self.user_id = new_id
            self.password = password_get()
        
        super(singupdata,self).save(*args, **kwargs)
        