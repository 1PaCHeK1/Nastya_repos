from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import OnlyManager


class User(AbstractUser):
    manager_objects = OnlyManager()
    patronymic = models.CharField('Отчество',
        max_length=255,
        blank=True
    )
    ROLE_STATUS = ((0, 'Клиент'), (1, 'Менеджер'), (2, 'Админ'))
    role = models.PositiveSmallIntegerField(choices=ROLE_STATUS, default=0)
    RECEIVE_NEWSLETTERS_STATUS = ((1, 'Получать рассылку'), (2, 'Не получать рассылку'))
    receive_newsletter = models.PositiveSmallIntegerField(choices=RECEIVE_NEWSLETTERS_STATUS, default=1)
    points = models.IntegerField('Баллы', default=0)
    

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
        

class UserManager(models.Model):
    user = models.ForeignKey("User", verbose_name="Клиент", on_delete=models.SET_NULL, null=True, related_name="usermanager_user")
    manager = models.ForeignKey("User", verbose_name="Менеджер", on_delete=models.SET_NULL, null=True, related_name="usermanager_manager")

    def __str__(self) -> str:
        return self.user.username + ' - ' + self.manager.username
    
    class Meta:
        verbose_name = 'Клиент - Менеджер'


class ReferalUser(models.Model):
    user_from = models.ForeignKey("User", verbose_name="Пригласивший пользователь", on_delete=models.SET_NULL, null=True, related_name="referaluser_userfrom")
    user_to = models.OneToOneField("User", verbose_name="приглашенный пользователь", on_delete=models.SET_NULL, null=True, related_name="referaluser_userto")

    def __str__(self) -> str:
        return self.user_from.username + ' -> ' + self.user_to.username
    
    class Meta:
        verbose_name = 'Реферальные клиенты'
