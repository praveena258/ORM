from django.db import models
from django.contrib import admin
class Book(models.Model):
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=50)
    coauthor=models.CharField(max_length=25)
    genre=models.CharField(max_length=100)
    price=models.IntegerField()
    
class BookAdmin(admin.ModelAdmin):
    list_display=('name','author','coauthor','genre','price')

# Create your models here.
