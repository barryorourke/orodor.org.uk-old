#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Barry O'Rourke"
EMAIL = u"barry@orodor.org.uk"
SITENAME = u'orodor.org.uk'
SITEURL = 'http://localhost:8000'
TIMEZONE = 'Europe/London'

DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'en'

THEME = '../pelican-orodor'
STATIC_PATHS = ['css', 'fonts', 'images', 'js']

# social links
SOCIAL = (
    ('twitter', 'https://www.twitter.com/barryorourke'),
    ('github', 'https://www.github.com/barryorourke'),
    ('tumblr', 'http://fuckyeahhemiplegia.tumblr.com'),
    ('flickr', 'https://www.flickr.com/photos/barryorourke'),
)

# feed settings
FEED_ATOM = "feed/atom.xml"

# do not generate
ARCHIVES_SAVE_AS      = None
AUTHOR_SAVE_AS        = None
AUTHORS_SAVE_AS       = None
CATEGORY_SAVE_AS      = None
CATEGORIES_SAVE_AS    = None
TAGS_SAVE_AS          = None
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None

# article urls
ARTICLE_URL     = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# page urls
PAGE_URL        = '{slug}/'
PAGE_SAVE_AS    = '{slug}/index.html'

# tag urls
TAG_URL         = 'tag/{slug}/'
TAG_SAVE_AS     = 'tag/{slug}/index.html'

# pagination
DEFAULT_PAGINATION = 5

# set the url pattern for paginated pages
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['sitemap', 'gzip_cache']
