from django.db import models
from django.contrib.auth.models import User


class Weather(models.Model):
    city_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, editable=False)

    def __str__(self):
        return self.city_name
# Create your models here.
