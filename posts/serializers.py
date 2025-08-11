from rest_framework import serializers
from .models import Post, Contact


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'created_at', 'title', 'body', 'image')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("id", "name", "email", "subject", "created_at")

