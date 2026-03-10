from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="blogs"
    )

    short_description = RichTextField()

    content = RichTextField()

    cover_image = models.ImageField(upload_to="blogs/")

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    published_date = models.DateField()

    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title