from django.db import models
from datetime import datetime
from users.models import User


class Tag(models.Model):
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    author = models.ForeignKey(User, 
                               on_delete=models.SET_NULL,
                               null=True)

    tags = models.ManyToManyField(Tag)
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('Url статьи', unique=True)
    text = models.TextField('Текст статьи')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    creator = models.ForeignKey(User, 
                                on_delete=models.SET_NULL,
                                null=True)
    article = models.ForeignKey(Article,  
                                on_delete=models.CASCADE,
                                null=True)
    text = models.TextField('Текст комментария')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return str(self.creator.username) + " " + str(self.article.title)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'