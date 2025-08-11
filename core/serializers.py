from rest_framework import serializers
from .models import Lab, LabImage, LabExtra,ContactMessage

class LabImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabImage
        fields = ['image']

class LabImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabImage
        fields = ['id', 'image']

class LabExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabExtra
        fields = ['title', 'description', 'goal', 'contents', 'system']

class LabSerializer(serializers.ModelSerializer):
    images = LabImageSerializer(many=True, read_only=True)
    extra = LabExtraSerializer(read_only=True)

    class Meta:
        model = Lab
        fields = [
            'id', 'key', 'title', 'description', 'detail',
            'color', 'background', 'text_color', 'images', 'extra'
        ]
class LabExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabExtra
        fields = ['title', 'description', 'goal', 'contents', 'system']

class LabSerializer(serializers.ModelSerializer):
    images = LabImageSerializer(many=True, read_only=True)
    extra = LabExtraSerializer(read_only=True)

    class Meta:
        model = Lab
        fields = [
            'id', 'key', 'title', 'description', 'detail',
            'color', 'background', 'text_color', 'images', 'extra'
        ]

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']