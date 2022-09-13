from django.contrib import admin
from .models import (
    Chat,
    Notification,
    Message
)

# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    display_list = "__all__"