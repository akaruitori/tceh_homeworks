from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count, Avg, FloatField, F
from .models import BlogPostModel, CommentModel
from .forms import BlogPostForm, CommentForm


def index(request):
    # На главной странице посты упорядочены по дате,
    # от новых к старым.
    if request.method == 'GET':
        posts = BlogPostModel.objects.all().order_by('-date')
        return render(request, 'blog17/index.html', {'posts': posts})
    return HttpResponse(status=405)


def post_view(request, post_id):
    # Страница просмотра поста, тут же форма для комментариев
    # и сами комментарии.
    post = get_object_or_404(BlogPostModel, pk=post_id)
    comments = CommentModel.objects.filter(post=post)
    comment_form = CommentForm()
    c = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        # Если форма валидна, сохраняем комментарий,
        # а юзеру показываем ту же страницу с новым комментарием.
        if comment_form.is_valid():
            comment_form.save(post=post)
            return render(request, 'blog17/post.html', c)

    elif request.method == 'GET':
        return render(request, 'blog17/post.html', c)
    return HttpResponse(status=405)


def new_post(request):
    # Тут просто формочка для нового поста.
    if request.method == 'GET':
        form = BlogPostForm()
        return render(request, 'blog17/new_post.html', {'form': form})
    elif request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # В случае получения валидного поста, перенаправляем юзера
            # на страницу нового поста.
            post = form.save(BlogPostModel)
            return redirect('post', post.pk)
        else:
            return render(request, 'blog17/new_post.html', {'form': form})
    return HttpResponse(status=405)


def stats(request):
    if request.method == 'GET':

        # Задание: показать среднее количество комментариев на пост.
        comm_per_post = BlogPostModel.objects.annotate(
            num_comments=Count('comments')).aggregate(Avg('num_comments'))

        # А второе задение, получить кол-во постов в каждом месяце,
        # одним выражение сделать не получается.
        # Нужен намек на правильное наравление :)
        return render(request, 'blog17/stats.html', {
            'avg_comments': comm_per_post['num_comments__avg']
        })
    return HttpResponse(status=405)
