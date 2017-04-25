from django import forms
from .models import BlogPostModel, CommentModel


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ('author', 'title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('name', 'text',)

    def save(self, commit=True, post=None):
        # Скопировано из пицца-проекта :)
        inst = super().save(commit=False)
        inst.post = post
        if commit:
            inst.save()
        return inst

