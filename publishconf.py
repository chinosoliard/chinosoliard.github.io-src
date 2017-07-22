#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.chinosoliard.com'
RELATIVE_URLS = False

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'feeds/'
FEED_ATOM = 'feeds/atom/feed.xml'
FEED_RSS = 'feeds/rss/feed.xml'
FEED_ALL_ATOM = 'feeds/atom/all.xml'
FEED_RSS_ATOM = 'feeds/rss/all.xml'
CATEGORY_FEED_ATOM = 'feeds/atom/category-%s.xml'
CATEGORY_FEED_RSS = 'feeds/rss/category-%s.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
