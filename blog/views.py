from django.shortcuts import render
from .models import Blog
import json
from django.core import serializers

from django.http import Http404
from django.http import JsonResponse
from .forms import CommentForm
from .models import Comment
import time
# Create your views here.

blogListPageConfig = {
    #blog首页打开时默认显示n条
    'default_blogs': 2,
    #ajax请求更多blog时，一次请求返回n条
    'ajax_blogs':1,
    #执行了几次get_more_blogs_by_ajax
    'more_blogs_count': 0,
    #每条blog的摘要长度
    'abstract_length':3
}
def reset_blog_list_page_config():
    blogListPageConfig['more_blogs_count'] = 0


def get_blogs(request):
    reset_blog_list_page_config()
    # 取得打开页面要默认显示的那几条博客
    blogs = Blog.objects.all().order_by('-created')[:blogListPageConfig['default_blogs']]
    #声明一个list来放置要首页默认显示的blogs
    blog_list = []
    #这里对blogs切片，默认显示n条blog，其他的用ajax刷新出来，避免blog多的时候加载缓慢
    for item in blogs:
        blog = {
            'id': item.id,
            'title': item.title,
            'author': item.author,
            'created': item.created.strftime("%Y-%m-%d %H:%M:%S") ,
            #这里对blog内容切片生成摘要
            'abstract': item.content[:blogListPageConfig['abstract_length']],
        }
        blog_list.append(blog)
    json_blog_list = {
        'blogList':blog_list
    }
    return render(request,'blog-list.html',{
        'Blogs':json.dumps(json_blog_list),
    })

def get_more_blogs_by_ajax(request):
    #计算并取出需要的blogs
    start = blogListPageConfig['default_blogs'] + \
             blogListPageConfig['ajax_blogs'] * blogListPageConfig['more_blogs_count']
    end = start + blogListPageConfig['ajax_blogs']
    #is_more用来记录后台是否还有更多的blogs
    is_more_blog = True
    if( end >= Blog.objects.all().__len__() ):
        end = None
        is_more = False
    blogs = Blog.objects.all().order_by('-created')[start:end]
    # 计数，该函数执行了一次
    blogListPageConfig['more_blogs_count'] += 1
    #生成要返回的数据
    blog_list = []
    for item in blogs:
        blog = {
            'id': item.id,
            'title': item.title,
            'author': item.author,
            'created': item.created.strftime("%Y-%m-%d %H:%M:%S"),
            # 这里对blog内容切片生成摘要
            'abstract': item.content[:blogListPageConfig['abstract_length']],
        }
        blog_list.append(blog)

    json_blog_list = {
        #当is_more为False的时候，说明后台没有更多的blogs了
        'is_more_blog':is_more_blog,
        'blogList': blog_list
    }
    return JsonResponse( json.dumps(json_blog_list) )



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