from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import Postform

# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/list.html", context)


def create(request):
    if request.method == "POST":
        forms = Postform(request.POST)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:detail", post.pk)
    else:
        forms = Postform()
    context = {"forms": forms}
    return render(request, "blog/create.html", context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "blog/detail.html", context)
