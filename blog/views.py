from django.shortcuts import render
from .models import Blog
from .models import Tag
from .models import Category
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
    'default_blogs': 3,
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
    if( end >= Blog.objects.all().__len__() ):
        end = None
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
    #ajax返回的response对象不用转json，由前端js来把response对象中的body转成json
    more_blogs = {
        'blogList': blog_list
    }
    return JsonResponse( more_blogs )


def get_detail(request, blog_id):
    reset_blog_list_page_config()
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    #判断请求方法，若是post，存入数据库
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog_id'] = blog_id
            Comment.objects.create(**cleaned_data)
    #取得detail页面相关信息并返回
    #得到blog的tags构成的tag_list
    tags = blog.tags.all()
    tag_list = []
    for tag in tags:
        tag_dict = {
            'id':tag.id,
            'name':tag.name
        }
        tag_list.append(tag_dict)
    #得到blog的comment构成的comment_list
    comments = blog.comment_set.all()
    comments_list = []
    for comment in comments:
        comment_dict = {
            'id': comment.id,
            'name': comment.name,
            'content': comment.content,
            'created': comment.created.strftime("%Y-%m-%d %H:%M:%S"),
        }
        comments_list.append(comment_dict)
    aaa = blog.created.astimezone()
    blog_info = {
        'id': blog.id,
        'title': blog.title,
        'author': blog.author,
        'created': blog.created.strftime("%Y-%m-%d %H:%M:%S"),
        'content': blog.content,
        'category':{
            'categoryId': blog.category_id,
            'categoryName': blog.category.name
        },
        'tags':tag_list,
        'comments':comments_list
    }
    return render(request, 'blog-detail.html', {
        'blogDetail':json.dumps(blog_info),
    })