#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Barry O'Rourke"
EMAIL = u"barry+site@orodor.org.uk"
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
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# pagination
DEFAULT_PAGINATION = 5
