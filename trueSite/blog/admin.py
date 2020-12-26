from django.contrib import admin
from .models import Post, PostImages, SocialShares

class PostImageAdmin(admin.StackedInline):
    model = PostImages

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    prepopulated_fields = {'slug': ('title', )}
    inlines = [PostImageAdmin]
    list_per_page = 10

    class Meta:
        model = Post

@admin.register(PostImages)
class PostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialShares)
class SocialShare(admin.ModelAdmin):
    list_display = ['name', 'share_source']
