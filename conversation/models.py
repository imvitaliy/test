from django.db import models

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Sentence(models.Model):
   title = models.CharField(max_length=500)
   sentence = models.TextField(blank=True)

class SentenceCounter(models.Model):
   sentence_number = models.IntegerField()
   sentences = models.TextField(blank=True)
