from django.db import models

class Url(models.Model):
    original_url = models.TextField(True)
    short_url = models.CharField(max_length=20, unique=True)
