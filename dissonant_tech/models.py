from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

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


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)

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
        super(BlogPost, self).save(*args, **kwargs)


