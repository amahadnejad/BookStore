from django.contrib import admin

from .models import Book, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'recommend', 'datetime_created', 'is_active', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'author', 'price', 'cover', 'datetime_created', 'datetime_modified', )
