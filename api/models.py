from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

class Palette(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    visibilty = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])

    
