import datetime
from django.test import TestCase
from dissonant_tech.models import BlogPost, Category

class BlogPostTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(id=1,
                title = 'BlogPostTestCase number one',
                posted = datetime.datetime.now(),
                category = 'Testing')
        BlogPost.objects.create(id=2,
                title = 'Tetst number two',
                category = 'Testing')

    def test_post_have_category(self):
        first_post = Post.objects.get(id=1)
        second_post = Post.objects.get(id=2)
        self.assertEqual(first_post.category, 'Testing')
        self.assertEqual(second_post.category, 'Testing')
