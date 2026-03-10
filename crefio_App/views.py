from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, BlogPost
from .serializers import CategorySerializer, BlogPostSerializer,ContactSerializer
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status




# View all categories
@api_view(['GET'])
def category_list(request):

    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)



# View all blog 
@api_view(['GET'])
def blog_list(request):

    blogs = BlogPost.objects.all()

    serializer = BlogPostSerializer(blogs, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    serializer = BlogPostSerializer(blog)
    return Response(serializer.data)


@api_view(['POST'])
def contact_form(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        mobile = serializer.validated_data['mobile']
        message = serializer.validated_data['message']

        # Compose email
        subject = f'New Contact Form Submission from {name}'
        email_message = f"Name: {name}\nEmail: {email}\nMobile: {mobile}\nMessage: {message}"

        # Send email
        send_mail(
            subject,
            email_message,
            settings.EMAIL_HOST_USER,        
            ['bpritiranjan16@gmail.com'],        
            fail_silently=False,
        )

        return Response({'success': 'Email sent successfully!'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


