from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from posts.models import Post, Comment, Like
from .forms import PostForm, CommentForm


@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:post_detail', post_slug=new_post.slug)
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


def post_list_view(request):
    posts = Post.objects.filter(is_published=True).select_related('author').prefetch_related('likes', 'comments')
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, is_published=True)
    comments = post.comments.select_related('author').all()
    likes_count = post.likes.count()
    user_liked = post.likes.filter(user=request.user).exists() if request.user.is_authenticated else False

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('posts:post_detail', post_slug=post.slug)
        else:
            return redirect('users:login')
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'likes_count': likes_count,
        'user_liked': user_liked,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_update_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if post.author != request.user:
        return HttpResponseForbidden("Ошибка 403, у вас нет прав на редактирование этого поста.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {'form': form, 'is_edit': True})


@login_required
def post_delete_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if post.author != request.user:
        return HttpResponseForbidden("Ошибка 403, у вас нет прав на удаление этого поста.")

    if request.method == "POST":
        post.delete()
        return redirect('posts:post_list')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})


@login_required
def post_like_toggle_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, is_published=True)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('posts:post_detail', post_slug=post.slug)
