from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    # New: tags per post
    # Using a simple Tag model with a many-to-many relation
    # Keep it optional and easy to manage via API/admin
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>: {self.subject}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


# Define the many-to-many after Tag to avoid forward reference issues
Post.add_to_class('tags', models.ManyToManyField('Tag', related_name='posts', blank=True))
