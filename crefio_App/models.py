from django.db import models
from ckeditor.fields import RichTextField


# ------------------------Category Model------------------------


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# ------------------------BlogPost Model------------------------


class BlogPost(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    Category = models.ForeignKey(
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
    

    
# ------------------------Contact Model------------------------

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# ------------------------JobPost Model------------------------

class JobPost(models.Model):
    role = models.CharField(max_length=200)
    job_description = models.TextField()
    qualification = models.TextField()
    locations = models.CharField(max_length=255)
    additional_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role

# ------------------------JobApplication Model------------------------

class JobApplication(models.Model):
    role_applied_for = models.ForeignKey(
        JobPost,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    name = models.CharField(max_length=150)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    additional_information = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role_applied_for.role}"

