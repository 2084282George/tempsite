from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify

class Show(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    slug = models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Show, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Shows'

    def __str__(self):
        return self.name

class Episode(models.Model):
    show = models.ForeignKey(Show)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    date = models.DateField(default=0)

    class Meta:
        verbose_name_plural = 'Episodes'

    def __str__(self):
        return self.title
