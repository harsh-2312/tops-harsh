from .models import *
from rest_framework import serializers

class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['created_at','updated_at']
