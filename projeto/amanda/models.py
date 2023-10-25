# from django.contrib.auth.models import User
from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name