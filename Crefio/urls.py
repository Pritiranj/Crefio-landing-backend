"""
URL configuration for Crefio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from crefio_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # show all categories
    path('categories/', category_list, name='category_list'),

    # show all blog posts
    path('blogs/', blog_list, name='blog_list'),

    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),
    
    path('contact/', contact_form, name='contact_form'),
    path('contacts/', contact_list, name='contact_list'),

    path('job/', job_post, name='job_post'),
    path('job/<int:pk>/', job_post, name='job_detail'),

    path('applications/', job_application, name='job_application'),
    path('applications/<int:pk>/', job_application, name='job_application_detail'),

    
]