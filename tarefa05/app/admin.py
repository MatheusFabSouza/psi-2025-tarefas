from django.contrib import admin
from .models import Post, Blog

class PostAdmin(admin.ModelAdmin):
    display = ('titulo', 'data_pub')
    ordem     = ('data_pub',)
admin.site.register(Blog)
admin.site.register(Post)