from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Comment, Post


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog_index.html', {'posts': posts})


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')

    context = {
        'posts': posts,
        'category': category
    }

    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post).order_by('-created_on')[:5]
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'comments_count': comments.count()
    }

    return render(request, 'blog_detail.html', context)
