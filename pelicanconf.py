# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'chinosoliard'
SITENAME = u'Chino Soliard'
SUBTITLE = u'IT specialist | FOSS enthusiast | Fedora Contributor'
SITEURL = ''

TIMEZONE = 'America/Argentina/Buenos_Aires'


PATH = 'content'
PAGE_PATH = 'pages'
ARTICLE_PATH = 'blog'
STATIC_PATHS = ['images/article','images/galleries','images/static','images/widgets','files']
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{slug}-{lang}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{slug}-{lang}.html'
ARTICLE_LANG_URL = 'blog/{date:%Y}/{date:%b}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{slug}-{lang}.html'
ARTICLE_EXCLUDES = ['images/galleries']
PAGE_EXCLUDES = ['images/galleries']


PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_SORTING = 'size'
TAG_CLOUD_BADGE = False


THEME = './responsive-cli-pelican-theme'

IMAGE1= 'images/widgets/fedora.png'
LINK1= 'http://www.fedoraproject.org'
LINK1TITLE= 'Fedora Project'

IMAGE2= 'images/widgets/lugparana.png'
LINK2= 'http://www.lugparana.org'
LINK2TITLE= 'Linux User Group Paraná (Argentina)'

IMAGE3= 'images/widgets/sysarmy.png'
LINK3= 'http://sysarmy.com.ar/'
LINK3TITLE= 'sysarmy - El soporte de los que dan soporte'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 5
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Feed generation is usually not desired when developing
#FEED_DOMAIN = 'feeds/'
#FEED_ATOM = 'feeds/atom/feed.xml'
#FEED_RSS = 'feeds/rss/feed.xml'
#FEED_ALL_ATOM = 'feeds/atom/all.xml'
#FEED_RSS_ATOM = 'feeds/rss/all.xml'
#CATEGORY_FEED_ATOM = 'feeds/atom/category-%s.xml'
#CATEGORY_FEED_RSS = 'feeds/rss/category-%s.xml'
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Fedora Project', 'http://www.fedoraproject.org'),
         ('LUG Paraná (AR)', 'http://www.lugparana.org'),
         ('Python', 'http://www.python.org'),
         ('SysArmy', 'http://www.sysarmy.com.ar'),)

# Social widget
SOCIAL = (('Twitter', 'https://www.twitter.com/chinosoliard'),
          ('Facebook', 'https://www.facebook.com/chino.soliard'),
          ('LinkedIn', 'https://ar.linkedin.com/in/adriansoliard'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
