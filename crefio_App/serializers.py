from rest_framework import serializers
from .models import Category, BlogPost,Contact,JobPost, JobApplication

# -------------------------Category Serializer------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# -------------------------BlogPost Serializer------------------------

class BlogPostSerializer(serializers.ModelSerializer):
    Category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                read_only=False)
    class Meta:
        model = BlogPost
        fields = '__all__'

# -------------------------Contact Serializer------------------------


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


# -------------------------JobPost Serializer------------------------

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'


# -------------------------JobApplication Serializer------------------------

class JobApplicationSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role_applied_for.role', read_only=True)

    class Meta:
        model = JobApplication
        fields = '__all__'
    