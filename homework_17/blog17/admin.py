from django.contrib import admin
from .models import BlogPostModel, CommentModel


admin.site.register(BlogPostModel)
admin.site.register(CommentModel)
