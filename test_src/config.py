# -*- coding: utf-8 -*-
"""Blog Configuration
"""

# For Maverick
site_prefix = "/"
template = "Galileo"
index_page_size = 10
archives_page_size = 30
fetch_remote_imgs = False
enable_jsdelivr = {
    "enabled": False,
    "repo": "TripleYuan/tripleyuan.github.io@main"
}
locale = "Asia/Shanghai"
category_by_folder = False

# For site
site_name = "Yuan's Blog"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2025-03-20T16:00+08:00"
author = "Yuan"
email = "im.wuxiaoyuan@gmail.com"
author_homepage = "https://tripleyuan.github.io/"
description = "Hello, World!"
key_words = ["Java", "SpringBoot", "Yuan", "Blog"]
language = 'english'
external_links = [
    {
        "name": "TripleYuan",
        "url": "https://github.com/TripleYuan",
        "brief": "Keep learning and practicing."
    },
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/TripleYuan",
        "icon": "gi gi-github"
    },
]

# valine = {
#     "enable": True,
#     "el": '#vcomments',
#     "appId": "IKRAfuPq0zrz6Wfje8ahHAIP-gzGzoHsz",
#     "appKey": "lFaCWkd4xCs0Ng5UWs1eHNwU",
#     "visitor": True,
#     "recordIP": True
# }

head_addon = ''

footer_addon = ''

body_addon = ''
