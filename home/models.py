from django.db import models

# Create your models here.
class website(models.Model):
    url = models.CharField(max_length=50)
    status = models.BooleanField()