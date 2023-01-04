# -*- coding: utf-8 -*-
# This file is part of Viper - https://github.com/viper-framework/viper
# See the file 'LICENSE' for copying permission.

from django.urls import include, re_path
from django.contrib import admin

from viper.core.config import __config__

cfg = __config__


urlpatterns = [
    re_path(r'^', include('viper_web.viperweb.urls')),
    re_path(r'^', include('favicon.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/', include('viper_web.viperapi.urls')),
]
