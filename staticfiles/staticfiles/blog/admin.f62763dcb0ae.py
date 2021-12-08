from django.contrib import admin
from .models import Post, Comments


class CommentsInline(admin.TabularInline):
    model = Comments


class CommentsAdmin(admin.ModelAdmin):
    inlines = [
        CommentsInline,
    ]
    list_display = ("title", "author",)


admin.site.register(Post, CommentsAdmin)
