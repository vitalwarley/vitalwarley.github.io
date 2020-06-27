#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'vitalwarley'
SITENAME = 'vital.ai'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Maceio'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME = 'basic'
THEME = 'themes/basic'
GITHUB_URL = 'https://github.com/vitalwarley'

# Basic
DISPLAY_CATEGORIES_ON_MENU = False

# URL
AUTHORS_SAVE_AS = ''
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

AUTHOR_URL = 'blog/authors/{slug}/'
AUTHOR_SAVE_AS = 'blog/authors/{slug}.html'

CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'

# INDEX_URL = 'blog/'
# INDEX_SAVE_AS = 'blog/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = [
    'images', 
    # 'extra/robots.txt',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
