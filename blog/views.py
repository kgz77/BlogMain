from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm, LoginForm
from django.views.generic import View

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/fronpage.html', {'posts': posts})

def post_detail(request,slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request, Post)
        return render(request, 'blog/login.html', {'form': form})