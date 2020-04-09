from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)