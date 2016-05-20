#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-05-19 16:39 
@author: guolt
"""

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self,obj):
        return obj.publish

