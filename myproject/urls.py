#coding: utf8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from poll import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    #  namesapce防止在html页面中引用url的名称出现重复
    # 注意：使用namespace的时候必须加app_name的属性否则会报错！('str' object has no attribute 'regex')
    url(r'^poll/', include('poll.urls',namespace="author-polls",app_name='poll')),
    url(r'^admin/', include(admin.site.urls)),
)
