from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from django.utils.functional import cached_property


class Category(models.Model):

    """Category Model"""
    title = models.CharField(
        max_length=100,
        db_index=True,
        unique=True,
        verbose_name='Title',
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
        max_length=100,
        verbose_name='Title'
        )
    slug = models.SlugField(
        unique=True,
        verbose_name='Slug',
        help_text='Uri Identifier',
        max_length=255
        )
    content = models.TextField(
        verbose_name='Content (Markdown)',
        )
    date_publish = models.DateField(
        db_index=True,
        verbose_name='Publish Date'
        )
    published = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='Published',
        )
    categories = models.ManyToManyField(
        Category,
        verbose_name='Categories',
        blank=True
        )
    author = models.ForeignKey(
        User,
        verbose_name='User'
        )
    cover_image = models.ImageField(
        upload_to='articles/%Y/%m/',
        null=True
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
        super(Article, self).save(*args, **kwargs)

    @cached_property
    def as_json(self):
        categories = {}
        self_categories = self.categories.all()
        c_num = 1

        for c in self_categories:
            categories['category'+str(c_num)] = c.title

        return dict(
            title=self.title,
            date_publish=self.date_publish.isoformat(),
            content=self.content,
            published=str(self.published),
            categories=categories,
            author=self.author.get_full_name())
