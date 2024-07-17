from django import forms 
from .models import ProductCategory,singupdata,Brand

class mobileform(forms.ModelForm):
    class Meta:
        model = ProductCategory
        exclude = ('product_id','created','updated')

class userdata(forms.ModelForm):
    class Meta:
        model = singupdata
        fields = '__all__'

class Brandform(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']

class Mobiledata(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
