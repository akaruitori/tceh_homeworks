from django.shortcuts import render
from .models import Storage, BlogPostModel
from .forms import BlogPostForm
import logging

logger = logging.getLogger(__name__)


def home(request):
    storage = Storage()
    all_items = storage.items
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            model = BlogPostModel(form.cleaned_data)
            all_items.append(model)
        else:
            logger.error('Someone have submitted an incorrect form!')
    else:
        form = BlogPostForm()
    return render(request, 'home.html', {
                  'form': form, 'items': all_items
    })
