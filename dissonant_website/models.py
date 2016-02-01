from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):

    """Project Model"""
    name = models.CharField(
        max_length=100,
        db_index=True,
        unique=True,
        verbose_name='Name',
        )
    description = models.TextField(
        verbose_name='Description',
        )
    link = models.URLField(
        verbose_name='Link',
        )
    slug = models.SlugField(
        max_length=100,
        db_index=True,
        )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
