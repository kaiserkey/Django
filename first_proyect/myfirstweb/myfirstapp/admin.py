from django.contrib import admin

# import models
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('status', 'created_date', 'publish', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


# Register your models here.
admin.site.register(Post, PostAdmin)