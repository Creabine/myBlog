from django.db import models
from django import forms

# Create your models here.

# 这边要继承这个models.Model类，固定写法

class Category(models.Model):
    #分类
    name = models.CharField('名称',max_length=16)

class Tag(models.Model):
    #标签
    name = models.CharField('名称',max_length=16)

class Blog(models.Model):
    #博客
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)
    content = models.CharField('正文',max_length=140)
    created = models.CharField('发布时间',max_length=16,auto_created=True)

    category = models.ForeignKey(Category,verbose_name='分类')
    tags = models.ManyToManyField(Tag,verbose_name='标签')

class Comment(models.Model):
    #评论
    blog = models.ForeignKey(Blog,verbose_name='博客')
    name = models.CharField('称呼',max_length=16)
    content = models.CharField('内容',max_length=140)
    created = models.DateField('发布时间',auto_created=True)

class CommentForm(forms.Form):
    #评论表单
    name = forms.CharField(label='昵称',max_length=16,error_messages={
        'required':'请填写您的昵称',
        'max_length':'昵称太长了'
    })
    email = forms.EmailField(label='邮箱',error_messages={
        'required':'请填写您的邮箱',
        'invalid':'邮箱格式不正确'
    })
    content = forms.CharField(label='评论内容',error_messages={
        'required':'请填写您的评论内容',
        'max_length':'评论内容太长'
    })




