from django.db import models

from django.contrib.auth.models import User


class Sentence(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=500, unique=True)
   sentence = models.TextField(blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   modified_at = models.DateTimeField(auto_now=True)
