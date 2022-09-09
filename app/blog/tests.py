from django.test import TestCase
from users.models import User
from blog.models import Article, Tag


class CommentForArticle(TestCase):
    def setUp(self) -> None:
        self.author = User.objects.create(username="Author",
                                          email="author@gmail.com")
        self.tags = [Tag.objects.create(name=str(i))
                     for i in range(5)]

    def test_CreateArticle(self):
        article = Article.objects.create(
            author=self.author,
            slug="test-article",
            title='Test Article',
        )
        
        self.assertIsInstance(article, Article)
