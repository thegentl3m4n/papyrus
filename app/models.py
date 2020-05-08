from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

#class book(models.Model):
#    book_title = models.CharField(max_length=100)
#    author = models.CharField(max_length=100)


class post(models.Model):
    post_title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # pdf_version = models.
