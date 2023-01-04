# This file is part of Viper - https://github.com/viper-framework/viper
# See the file 'LICENSE' for copying permission.

from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views
from .forms import MyAuthenticationForm


urlpatterns = [
    # login/logout (accounts)
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='viperweb/user_login.html',
                                                           authentication_form=MyAuthenticationForm), name='login'),
    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(template_name='viperweb/logged_out.html'), name='logout'),

    # Main Page
    re_path(r'^$', views.MainPageView.as_view(), name='main_page'),
    re_path(r'^project/(?P<project>[^/]+)/$', views.MainPageView.as_view(), name='main-page-project'),  # Project Page (Main view)

    re_path(r'^about/', views.AboutView.as_view(), name='about'),
    re_path(r'^changelog/', views.ChangelogView.as_view(), name='changelog'),
    re_path(r'^config/$', views.ConfigView.as_view(), name='config-file'),
    re_path(r'^create/$', views.CreateProjectView.as_view(), name='create-project'),

    re_path(r'^project/default/cli/$', views.CliView.as_view(), name='cli-default'),
    re_path(r'^project/(?P<project>[^/]+)/cli/$', views.CliView.as_view(), name='cli'),

    re_path(r'^project/(?P<project>[^/]+)/file/(?P<sha256>[^/]+)/$', views.FileView.as_view(), name='file-view'),  # File Page
    re_path(r'^project/(?P<project>[^/]+)/file/$', views.FileView.as_view(), name='file-list'),  # File List

    re_path(r'^project/(?P<project>[^/]+)/file/(?P<sha256>[^/]+)/cuckoo/$', views.CuckooCheckOrSubmitView.as_view(), name='file-cuckoo-submit'),

    re_path(r'^project/(?P<project>[^/]+)/hex/$', views.HexView.as_view(), name='hex-view'),  # Hex View
    re_path(r'^project/(?P<project>[^/]+)/module/$', views.RunModuleView.as_view(), name='run-module'),  # Run Module Ajax

    re_path(r'^search/$', views.SearchFileView.as_view(), name='search-file'),  # Search
    re_path(r'^urldownload/', views.UrlDownloadView.as_view(), name='url-download'),  # Download from URL
    re_path(r'^yara/$', views.YaraRulesView.as_view(), name='yara-rules'),  # Yara


    re_path(r'^virustotal/$', views.VtDownloadView.as_view(), name='vt-download'),  # Download form Virustotal

]
