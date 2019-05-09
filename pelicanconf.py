#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'jhonatanmsc'
SITENAME = 'jhonatanmsc.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL =  {
    'github': 'https://github.com/jhonatanmsc',
    'medium': 'https://medium.com/@jhonmscosta',
    'linkedin': 'https://linkedin.com/in/jhonatan-matheus-998182126',
    'facebook': 'https://www.facebook.com/jhonmscosta',
    'email': 'jhonmscosta@gmail.com'
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True