from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from markdown import markdown

# Create your models here.


class Category(models.Model):
    """Category Model"""
    title = models.CharField(
            max_length=100,
            db_index=True,
            unique=True,
            verbose_name = 'Title',
            )
    slug = models.SlugField(
            max_length=100,
            db_index=True,
            )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    """Article Model"""
    title = models.CharField(
            max_length = 100,
            verbose_name = 'Title'
            )
    slug = models.SlugField(
            unique=True,
            verbose_name = 'Slug',
            help_text = 'Uri Identifier',
            max_length = 255
            )
    summary = models.TextField(
            max_length = 1275,
            verbose_name = 'Summary'
            )
    content_markup = models.TextField(
            verbose_name = 'Content (Markup)',
            )
    content_markdown = models.TextField(
            verbose_name = 'Content (Markdown)',
            )
    date_publish = models.DateField(
            auto_now_add=True,
            verbose_name = 'Publish Date'
            )
    categories = models.ManyToManyField(
            Category,
            verbose_name = 'Categories',
            null = True,
            blank = True
            )
    author = models.ForeignKey(
            User,
            verbose_name = 'User'
            )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (),
                {
                    'slug': self.slug,
                    })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.content_markup = markdown(self.content_markdown, ['codehilite'])
        super(Article, self).save(*args, **kwargs)

    def as_json(self):
        categories = {}
        self_categories = self.categories.all()
        c_num = 1

        for c in self_categories:
            categories['category'+str(c_num)] = c.title

        return dict(
                title = self.title,
                date_publish = self.date_publish.isoformat(),
                content_markdown = self.content_markdown,
                content_markup = self.content_markup,
                categories = categories)



