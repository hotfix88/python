"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# 2016.11.09 to github!

from django.conf.urls import include, url
from django.contrib import admin
from views import *





urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello/',hello),
    #url(r'^hello2/',hello2),
    #url(r'^hello3/',hello3),
#    url(r'',include(admin.site.urls)),
#    url(r'^admin/', include(admin.site.urls)),
]


'''
from django.conf.urls.defaults import *
from mysite.views import hello

urlpatterns = patterns('',
    ('^hello/$', hello),
)
'''
