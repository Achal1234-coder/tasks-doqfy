from django.db import models


class Snippet(models.Model):
    text = models.TextField()
    shareable_url = models.CharField(max_length=100, unique=True)
    secret_key = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Snippet {self.id}'
