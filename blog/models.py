from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EntryQuerySet(models.QuerySet):
    def published(self):
        return  self.filter(published=True)
class Entry(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    slug=models.SlugField(max_length=300, unique=True)
    publish=models.BooleanField(default=True)
    photo = models.ImageField(upload_to = Image, height_field = None, width_field = None, blank = True)
    created=models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    object=EntryQuerySet.as_manager()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name= "blog Entry"
        verbose_name_plural="blog Entries"
        ordering=["-created"]