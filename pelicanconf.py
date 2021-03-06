#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

AUTHOR = "Weilet"
SITEURL = "https://weilet.me"
SITENAME = "Weilet's blog"
SITE_SUMMARY = "A Pelican blog I use to write down something about coding, product unboxing and gaming"

# Saving Settings
PATH = "content"
CATEGORY_URL = "category/{name}.html"
TAG_URL = "tag/{name}.html"
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_SAVE_AS = TAG_URL

# Regional Settings
TIMEZONE = "Asia/Shanghai"
DATE_FORMATS = {"en": "%Y-%m-%d"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
	'extra/CNAME': {'path': 'CNAME'},
	'extra/robots.txt': {'path': 'robots.txt'}
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
	'sitemap',	
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
THEME = "easy"
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives']

# Feeds
FEED_RSS = "rss.xml"

DISQUS_FILTER = True
UTTERANCES_FILTER = True


# Google Analytics
ANALYSTIC_ID = "UA-157817775-1"
