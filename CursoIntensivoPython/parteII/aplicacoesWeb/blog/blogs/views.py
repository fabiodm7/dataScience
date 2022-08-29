from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostEntry

# Create your views here.
def index(request):
    """Página inicial do blog"""
    return render(request,'blogs/index.html')

def blogposts(request):
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {'blogposts':blogposts}
    return render(request,'blogs/blogposts.html',context)

def check_owner_post(request,registro):
    if registro.owner != request.user:
        raise Http404

@login_required
def new_post(request):
    """Adiciona um novo post"""
    if request.method != 'POST':
        form = BlogPostEntry()
    else:
        form = BlogPostEntry(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:blogposts'))

    context = {'form':form}
    return render(request,'blogs/new_post.html',context)

@login_required
def edit_post(request,blogpost_id):
    """Edita um post"""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    check_owner_post(request,blogpost)

    if request.method != 'POST':
        form = BlogPostEntry(instance=blogpost)
    else:
        form = BlogPostEntry(instance=blogpost,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogposts'))

    context = {'blogpost':blogpost,'form':form}
    return render(request,'blogs/edit_post.html',context)