# *a language app, software, tool, resource, etc.*

from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
