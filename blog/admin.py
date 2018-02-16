# blog/admin.py
from django.contrib import admin
from .models import Post
# Register your models here.

# 첫번째 방법
# admin.site.register(Post)

# 두번째 방법
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'created_at', 'updated_at']

# admin.site.register(Post, PostAdmin)

# 세번째 방법
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']

