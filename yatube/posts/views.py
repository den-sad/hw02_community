from django.shortcuts import render, get_object_or_404
from .models import Post, Group


LAST_SHOWING_POSTS: int = 10


def index(request):
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:LAST_SHOWING_POSTS]
    context = {
        'title': title,
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:LAST_SHOWING_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
