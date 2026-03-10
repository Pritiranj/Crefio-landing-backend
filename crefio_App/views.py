from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, BlogPost
from .serializers import CategorySerializer, BlogPostSerializer


# View all categories
@api_view(['GET'])
def category_list(request):

    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)



# View all blog posts
@api_view(['GET'])
def blog_list(request):

    blogs = BlogPost.objects.all()

    serializer = BlogPostSerializer(blogs, many=True)

    return Response(serializer.data)

    



