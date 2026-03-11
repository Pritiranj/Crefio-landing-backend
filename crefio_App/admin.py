from django.contrib import admin
from .models import Category, BlogPost,Contact,JobApplication,JobPost


admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Contact)
admin.site.register(JobPost)
admin.site.register(JobApplication)
