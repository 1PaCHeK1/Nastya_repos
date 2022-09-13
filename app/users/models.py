from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    patronymic = models.CharField('Отчество',
        max_length=255,
        blank=True
    )
    ROLE_STATUS = ((0, 'Клиент'), (1, 'Менеджер'), (2, 'Админ'))
    role = models.PositiveSmallIntegerField(choices=ROLE_STATUS, default=0)


class Tag(models.Model):
    name = models.CharField('Название',
        unique=True,
        max_length=255,
        blank=False,
        null=False,
        help_text="Обязательное поле"    
    )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug   = models.SlugField('Url', 
        max_length=255,
        blank=False,
        null=False,
        help_text="Обязательное поле"    
    )
    title  = models.CharField('Заголовок', 
        max_length=255,
        blank=False,
        null=False,
        help_text="Обязательное поле",
    )
    content = models.TextField("Контент")
    create_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return f"{self.title} – {self.id}"
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'