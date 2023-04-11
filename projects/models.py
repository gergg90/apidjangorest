from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    full_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)