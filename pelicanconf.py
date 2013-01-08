#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Michael Jacobsen"
SITENAME = u"scicomp.dk"
SITEURL = 'http://www.scicomp.dk'

PAGE_DIR= 'pages'

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

STATIC_PATHS = ['images','js','java','downloads','docs']

FILENAME_METADATA = '(?P<serial>\d{4}).*'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Extra menu items - added to pages
# MENUITEMS = (("About me", "About me"),)

DEFAULT_PAGINATION = False

THEME = './mytheme'

FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                 ('extra/favicon.ico', 'favicon.ico')
                 )

