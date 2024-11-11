from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(blank=False)
    is_published = models.BooleanField(blank=False)
    created_at = models.DateField(blank=False)


class Location(models.Model):
    name = models.CharField(max_length=256, blank=False)
    is_published = models.BooleanField(blank=False)
    created_at = models.DateField(blank=False)


class Post(models.Model):
    title = models.CharField(max_length=256, blank=False)
    text = models.TextField(blank=False)
    pub_date = models.DateField(blank=False)
    publisged = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,
                                    blank=True, related_name='posts')
                        
    category = models.ForeignKey(Location, on_delete=models.SET_NULL,
                                blank=False, related_name='posts')
