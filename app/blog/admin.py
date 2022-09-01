from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Tag, Comment

class AdminArticle(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Article, AdminArticle)

class AdminTag(admin.ModelAdmin):
    class Meta:
        fields = ('name', )

admin.site.register(Tag, AdminTag)

class AdminComment(SummernoteModelAdmin):
    summernote_fields = ('text', )

admin.site.register(Comment, AdminComment)
