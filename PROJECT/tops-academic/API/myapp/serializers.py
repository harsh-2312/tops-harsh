from rest_framework import serializers
from .models import Globalnote


class Globalnoteserializer(serializers.ModelSerializer):
    class Meta:
        model = Globalnote
        fields = "__all__"