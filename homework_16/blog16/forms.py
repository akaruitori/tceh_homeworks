from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=140, min_length=4)
    text = forms.CharField(
           max_length=3500, min_length=10, widget=forms.Textarea
    )
