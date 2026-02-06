from django.db import models
from django.conf import settings
from ..companies.models import Company
class Job(models.Model):
    STATUS_CHOICES = [(
        'applied','Applied'),
        ('interview','Interview'),
        ('offering','Offer'),
        ('rejected','Rejected'),]

    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='jobs')
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='jobs')
    salary=models.IntegerField(default=0)
    title=models.CharField(max_length=200)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='applied')

    applied_date=models.DateField()
    notes=models.TextField(blank=True)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"