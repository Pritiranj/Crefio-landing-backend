from rest_framework import serializers
from .models import Category, BlogPost


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class BlogPostSerializer(serializers.ModelSerializer):
    Category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                source='category',read_only=False)
    class Meta:
        model = BlogPost
        fields = '__all__'

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    mobile = serializers.CharField(max_length=15)
    message = serializers.CharField()