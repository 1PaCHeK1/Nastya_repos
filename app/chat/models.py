from django.db import models
from users.models import User



class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_chat")
    participant = models.ManyToManyField(User, related_name="participant_chat")

    TYPE_STATUS = ((0, 'Беседа'), (1, 'Обращение'))
    type = models.PositiveSmallIntegerField(choices=TYPE_STATUS, default=1)

    def __str__(self):
        return f"Чат {self.id}"

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

class Notification(models.Model):
    text = models.TextField("Текст уведомления")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, editable=False),
    checked = models.BooleanField("Простомтрено", default=False)
    url = models.URLField("URl")
    
    def __str__(self):
        return "Уведомление"

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_owner")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="message_chat")
    text = models.TextField("Текст сообщения")

    def __str__(self):
        return "Сообщение " + str(self.id)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщение'
