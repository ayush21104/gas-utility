from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Allow null for debugging
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Request by {self.customer} - {self.service_type}"


# Create your models here.
