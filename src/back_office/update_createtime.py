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

C_MAP = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}


def update():
    for item in Blog.objects.all():
        time_split = item.time.split(' ')
        if len(time_split) == 5:
            month = C_MAP[time_split[0]]
            day = time_split[1]
            year = time_split[3]
            res_time = time_split[4]
            new_time = f"{year}/{month}/{day} {res_time}"
            print(new_time)
            datetime_time = datetime.datetime.strptime(new_time, "%Y/%m/%d %H:%M")
            print(type(datetime_time))
            item.created = datetime_time
            item.save()
            print(item.created)


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv):
        print("update")
        update()
    else:
        print('error')