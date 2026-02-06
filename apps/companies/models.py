from django.db import models

from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    location = models.CharField(max_length=200)

    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='companies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
