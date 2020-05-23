from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # pdf_version = models.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
