from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

from markdown import markdown

# Create your models here.


class Category(models.Model):
    """Category Model"""
    title = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return "%s" % (self.title,)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    """Article Model"""
    title = models.CharField(
            max_length=100,
            verbose_name = 'Title'
            )
    slug = models.SlugField(
            unique=True,
            verbose_name = 'Slug',
            help_text = 'Uri Identifier',
            max_length = 255
            )
    content_markup = models.TextField(
            verbose_name = 'Content (Markup)',
            )
    content_markdown = models.TextField(
            verbose_name = 'Content (Markdown)',
            )
    date_publish = models.DateField(auto_now_add=True,
            verbose_name = 'Publish Date'
            )
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(
            Category,
            verbose_name = 'Categories',
            null = True,
            blank = True
            )

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (),
                {
                    'slug': self.slug,
                    })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + created_on)
            self.content_markup = markdown(self.content_markdown, ['codehilite'])
        super(Article, self).save(*args, **kwargs)


