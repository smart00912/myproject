#coding: utf8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    #  namesapce防止在html页面中引用url的名称出现重复
    url(r'^poll/', include('poll.urls',namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
