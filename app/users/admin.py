from django.contrib import admin
from .models import (
    User,
    Tag,
    Post,
    UserManager
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(UserManager)
class UserManagerAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    display_list = "__all__"
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    display_list = "__all__"