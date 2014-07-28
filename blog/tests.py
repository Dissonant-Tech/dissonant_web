import datetime
from django.test import TestCase
from blog.models import BlogPost, Category

class BlogPostTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(id=1,
                title = 'BlogPostTestCase number one',
                created_on = datetime.datetime.now(),
                category = 'Testing')
        BlogPost.objects.create(id=2,
                title = 'Tetst number two',
                category = 'Testing')

    def test_post_have_category(self):
        first_post = BlogPost.objects.get(id=1)
        second_post = BlogPost.objects.get(id=2)
        self.assertEqual(first_post.category, 'Testing')
        self.assertEqual(second_post.category, 'Testing')
