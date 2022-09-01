from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Tag

class AdminArticle(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Article, AdminArticle)

class AdminTag(admin.ModelAdmin):
    class Meta:
        fields = ('name', )

admin.site.register(Tag, AdminTag)
