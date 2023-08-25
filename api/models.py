from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Palette(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    
    def serialize(self):
        serializer = PaletteSerializer(data=self, many=True)
        if serializer.is_valid():
            return serializer
        return serializer.errors

class Color(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=[('dominant', 'Dominant'), ('accent', 'Accent')])
    palette_id = models.ForeignKey(Palette, on_delete=models.CASCADE)
    
	#Validate color type max members.
    def save(self,*args, **kwargs):
        if self.id == None:
            if self.type=='dominant' and Color.objects.filter(palette_id=self.palette_id, type='dominant').count() >= 2:
                raise ValidationError("Dominant Color cannot be greater than 2")
            if self.type=='accent' and Color.objects.filter(palette_id=self.palette_id, type='accent').count() >= 4:
                raise ValidationError("Accent Color cannot be greater than 4")
        return super(Color, self).save(*args, **kwargs)
    
    def serialize(self):
        serializer = ColorSerializer(data=self, many=True)
        if serializer.is_valid():
            return serializer
        return serializer.errors

class Favorite(models.Model):
    username = models.CharField(max_length=50)
    palette_id = models.IntegerField()
    
    def serialize(self):
        serializer = FavoriteSerializer(data=self, many=True)
        if serializer.is_valid():
            return serializer
        return serializer.errors

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = "__all__"
    
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"