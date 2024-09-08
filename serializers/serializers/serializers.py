from datetime import datetime
from rest_framework import serializers
from django.db import models

# Blueprint  for instance
class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
# Model
class CommentModel(models.Model):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=50)
    created = serializers.DateTimeField()



# serializer
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=50)
    created = serializers.DateTimeField()
    
    def create(self, validated_data):
        # return Comment(
        #     email=validated_data.get("email"),
        #     content=validated_data.get("content"),
        #     created=validated_data.get("created"),
        # )
        # return Comment(**validated_data)
        return CommentModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.email)
        instance.created = validated_data.get('created', instance.created)
        
        instance.save()
        return instance
        
    
    

