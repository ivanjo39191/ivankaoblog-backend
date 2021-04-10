#!/usr/bin/env python
# coding: utf-8

import datetime, os, sys, re

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
site_packages = os.path.join(PROJECT_ROOT, '../libs')
if site_packages not in sys.path:
    sys.path.insert(0, site_packages)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append('..')
import dotenv

dotenv.load_dotenv(os.path.join(os.path.dirname(PROJECT_ROOT), '../.env'), True)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import pymysql

pymysql.install_as_MySQLdb()

from django.db.utils import DatabaseError, IntegrityError
from django.db.models.fields import TextField
from django.conf import settings
import django

django.setup()
import requests, json
import django.db.backends.utils
from django.db import OperationalError
from django.core.files import File

import requests
from bs4 import BeautifulSoup
import urllib
import re
import html
from django.shortcuts import render, redirect
from blog.models import Blog, BlogType
import json
import time
from ckeditor_uploader.fields import RichTextUploadingField


def pixnetcrawler():
    link = 'http://ivanjo39191.pixnet.net/blog/post/43269858-Python%E5%9F%BA%E7%A4%8E%E7%A8%8B%E5%BC%8F%E5%AD%B8%E7%BF%92%E7%B4%80%E9%8C%84(%E4%B8%80)'
    crawler_do(link)


    # return redirect('home')
def crawler_do(link):
    url = link  #選擇網址
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'  #偽裝使用者
    headers = {'User-Agent': user_agent}
    data_res = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(data_res, timeout=20)
    sp = BeautifulSoup(data, "html.parser")
    #標題
    title = sp.find("li", {"class": "title"}).find("h2").text
    #內文
    contents = sp.find("div", {"class": "article-content-inner"})
    content = str(contents)
    #日期
    published = str(sp.find("li", {"class": "publish"}).text)
    #下一篇連結
    category = sp.find("div", {"class": "article-footer"}).find("a", href=re.compile('/blog/category')).text

    nextarticle = sp.findAll("a", {"class": "quick-nav--next"}, href=re.compile('http'))
    for n in nextarticle:
        nextlink = n['href']
        print(nextlink)
    print(title)
    print(content)
    print(category)
    print(published)
    sql(title, content, category, published)
    try:
        crawler_do(nextlink)
    except:
        print('結束')
        # return redirect('home.html')


def sql(title, content, category, published):
    blogtitle = title
    blogcontent = content
    blogtype = category
    blog_time = published

    try:
        typename = BlogType.objects.get(type_name=blogtype)
        print('存入分類')
    except:
        typename = BlogType.objects.create(type_name=blogtype)
        print('創建分類')
    typename.save()
    print(typename)

    try:
        blogdb = Blog.objects.get(title=blogtitle)
        blogdb.blogcontent = blogcontent
        blogdb.blogtype = typename
        blogdb.blog_time = blog_time

        blogdb.save()
        print('更新資料')
    except:
        blogdb = Blog.objects.create(title=blogtitle, content=blogcontent, type=typename, time=blog_time)
        blogdb.save()
        print('成功存入一筆資料')


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv):
        print("pixnetcrawler")
        pixnetcrawler()
    else:
        print('error')