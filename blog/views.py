from django.shortcuts import render
from .models import Blog
import json
from django.core import serializers

from django.http import Http404
from .forms import CommentForm
from .models import Comment
import time
# Create your views here.

def get_blogs(request):
     # ctx = {
     #     'blogs': Blog.objects.all().order_by('-created')
     # }

    blogs = Blog.objects.all().order_by('-created')
    blogList = []
    for item in blogs:
        blog = {
            'id': item.id,
            'title': item.title,
            'author': item.author,
            'created': item.created.strftime("%Y-%m-%d %H:%M:%S") ,
            'categoryId': item.category_id,
            'content': item.content
        }
        blogList.append(blog)
    jsonList = {
        'blogList':blogList
    }

    return render(request,'blog-list.html',{
        'Blogs':json.dumps(jsonList),
    })





def get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog-detail.html', ctx)