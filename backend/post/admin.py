from django.contrib import admin
from .models import Post
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at','updated_at')
    list_filter = ('user',)
    search_fields = ('title', 'user__email')  # Assuming you want to search by title and user's email
