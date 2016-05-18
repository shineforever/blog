#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-05-18 16:12 
@author: guolt
"""

from django import template


register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    """
    显示所有已经发布的文章的数量
    :return:
    """
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    """
    显示最新的文章，默认是5个
    :param count:
    :return:
    """
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
