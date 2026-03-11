from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from .models import Category, BlogPost,Contact,JobPost, JobApplication
from .serializers import CategorySerializer, BlogPostSerializer,ContactSerializer,JobPostSerializer, JobApplicationSerializer
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import EmailMessage





# --------------------------Category List View------------------------

@api_view(['GET'])
def category_list(request):

    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)



# --------------------------Blog List View------------------------


@api_view(['GET'])
def blog_list(request):

    blogs = BlogPost.objects.all()

    serializer = BlogPostSerializer(blogs, many=True)

    return Response(serializer.data)

# --------------------------Slug Detail View------------------------


@api_view(['GET'])
def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    serializer = BlogPostSerializer(blog)
    return Response(serializer.data)

# --------------------------Contact Form View------------------------



@api_view(['GET'])
def contact_list(request):
    contacts = Contact.objects.all().order_by('-id')
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# --------------------------Send Contact To Email of the Host------------------------

@api_view(['POST'])
def contact_form(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        contact = serializer.save()

        subject = "New Contact Form Submission"
        message = f"""
Name: {contact.name}
Email: {contact.email}
Mobile: {contact.mobile}
Message: {contact.message}
"""

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )

        return Response(
            {
                "message": "Contact saved successfully and email sent",
                "data": ContactSerializer(contact).data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def job_post(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            data = JobPost.objects.all()
            serializer = JobPostSerializer(data, many=True)
        else:
            data = JobPost.objects.get(pk=pk)
            serializer = JobPostSerializer(data)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'PUT':
        data = JobPost.objects.get(pk=pk)
        serializer = JobPostSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        data = JobPost.objects.get(pk=pk)
        data.delete()
        return Response({'message': 'Deleted successfully'})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def job_application(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            data = JobApplication.objects.all()
            serializer = JobApplicationSerializer(data, many=True)
        else:
            data = JobApplication.objects.get(pk=pk)
            serializer = JobApplicationSerializer(data)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            application = serializer.save()

            email = EmailMessage(
                'New Job Application Submitted',
                f'''
Name: {application.name}
Email: {application.email}
Role Applied For: {application.role_applied_for}
Additional Information: {application.additional_information}
''',
                'your_email@gmail.com',
                ['your_email@gmail.com']
            )

            if application.resume:
                application.resume.open('rb')
                email.attach(
                    application.resume.name.split('/')[-1],
                    application.resume.read(),
                    'application/octet-stream'
                )

            email.send(fail_silently=False)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    if request.method == 'PUT':
        data = JobApplication.objects.get(pk=pk)
        serializer = JobApplicationSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        data = JobApplication.objects.get(pk=pk)
        data.delete()
        return Response({'message': 'Deleted successfully'})