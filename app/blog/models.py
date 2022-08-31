from django.db import models

from users.models import User


class Tag(models.Model):
    name = models.CharField('Название', max_length=50)


class Article(models.Model):
    author = models.ForeignKey(User, 
                               on_delete=models.SET_NULL,
                               null=True)

    tags = models.ManyToManyField(Tag)
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('Url статьи', unique=True)
    text = models.TextField('Текст статьи')