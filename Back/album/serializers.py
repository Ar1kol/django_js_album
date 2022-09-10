from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image # Table
        fields = "__all__" #all columns of the table