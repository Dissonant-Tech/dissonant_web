from django.contrib.auth.models import User
import datetime
from django.test import TestCase
from blog.models import Article, Category

class ArticleTestCase(TestCase):
    def setUp(self):
        self._user = User.objects.create_user(
                username = 'testUser',
                email = 'testEmail@email.com',
                password = 'testPassword',
                )
        self._category = Category.objects.create(
                title = 'Testing'
                )
        Article.objects.create(id=1,
                title = 'Test number one',
                summary_markdown = '##SUMMARY test',
                content_markdown = '#CONTENT test',
                author = self._user,
                published = True,
                )
        Article.objects.create(id=2,
                title = 'Test number two',
                summary_markdown = '##SUMMARY test',
                content_markdown = '#CONTENT test',
                author = self._user,
                published = False,
                )

    def test_post_have_category(self):
        first_post = Article.objects.get(id=1)
        second_post = Article.objects.get(id=2)
        self.assertEqual(first_post.title, 'Test number one')
        self.assertEqual(second_post.title, 'Test number two')
        
        self.assertEqual(first_post.published, True)
        self.assertEqual(second_post.published, False)
