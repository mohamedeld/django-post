from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
# Create your views here.

def post_list(request):
    all_post = Post.objects.all()

    return render(request,'blog_app/post_list.html',context={
        'all_post':all_post,
    })


def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'blog_app/post_detail.html',{'post':post})


def post_create(request):
    if request.method == 'POST':

        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')

    else:
        form = PostForm()

    return render(request,'blog_app/post_create.html',{
        'form':form,
    })

def post_edit(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/blog')

    else:
        form = PostForm(instance=post)

    return render(request,'blog_app/post_edit.html',{
        'form':form,
    })

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','content','created_at']
    template_name = 'blog_app/post_edit.html'
    success_url = '/blog/cbv'

class PostCreate(CreateView):
    model = Post
    fields = ['title','content','created_at','email','view_count']
    template_name = 'blog_app/post_create.html'
    success_url = '/blog/cbv'
