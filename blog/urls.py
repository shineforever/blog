#! /usr/bin/env python
# coding:utf-8
from django.conf.urls import url
from . import views
"""
Created on: 2016-04-19 16:50 
@author: guolt
"""

urlpatterns = [
    # post views
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
    r'(?P<post>[-\w]+)/$',
    views.post_detail,
    name='post_detail'),
]

