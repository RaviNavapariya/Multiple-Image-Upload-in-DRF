from dataclasses import field
from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        model = ImageModel
        fields = ['id','owner','image']

class GETPersonDetailSerializer(serializers.ModelSerializer):
    owner = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = PersonDetailModel
        fields = ['id','name','email','date_of_birth','owner']

class PersonDetailSerializer(serializers.ModelSerializer):
    image = serializers.ListField()
    class Meta:
        model = PersonDetailModel
        fields = ['id','name','email','date_of_birth','image']

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data
        instance = PersonDetailModel.objects.create(**data)
        for i in image:
            image = ImageModel.objects.create(image=i, owner=instance)
        return instance
