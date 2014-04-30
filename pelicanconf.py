#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Barry O'Rourke"
AUTHOR_BIO = u"ageing goth, fat dad and sysadmin with mild hemiplegia."
EMAIL = u"barry@orodor.org.uk"
GRAVATAR= 'http://www.gravatar.com/avatar/5329ca9e55a5d22091ae92dda3340a1c.png'
SITENAME = u'orodor.org.uk'
SITEINFO = AUTHOR_BIO
SITEURL = 'http://localhost:8000'
TIMEZONE = 'Europe/London'

ISSO_SERVER = "comments.orodor.org.uk"

DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'en'

THEME = '../pelican-crisp-bootstrap'
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
DEFAULT_PAGINATION = 8 

# set the url pattern for paginated pages
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['assets', 'sitemap', 'gzip_cache']

# sitemap configuration
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
