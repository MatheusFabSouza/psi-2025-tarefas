from django.contrib import admin
from .models import Post, Blog

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    display = ('titulo', 'data_pub')
    ordem     = ('data_pub',)
admin.site.register(Blog)