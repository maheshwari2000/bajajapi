from django.db import models
from django.db.models import query

# Create your models here.

class Bajaj(models.Model):
    is_success = models.CharField(default="true", max_length=150, editable=False)
    user_id = models.CharField(max_length=150, default="john_doe_17091999", editable=False)
    numbers = models.CharField(max_length=266)
    odd = models.CharField(max_length=266, null=True, blank=True, editable=False)
    even = models.CharField(max_length=266, null=True, blank=True, editable=False)

    def __str__(self):
        return self.numbers

