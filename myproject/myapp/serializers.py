#Importing serializers module from Django REST framework
from rest_framework import serializers

# importing Book model
from .models import Comment

# Defining a serializer for the Comment model
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # specifying the fields
        fields = ['id','text','author','created_at']