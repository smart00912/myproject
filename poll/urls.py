#coding: utf8
from django.conf.urls import patterns, include, url
from poll import views

# 其中的name的作用是在html页面中的url标签里指定跳转用的
urlpatterns = patterns('',
    # 通用视图写法
    url(r'^$',views.IndexView.as_view(),name='index'),                   
    url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/result/$',views.ResultView.as_view(),name='result'),
    url(r'^(?P<pk>\d+)/vote/$',views.vote,name='vote'),
    '''
    url(r'^$',views.index,name='index'),                   
    url(r'^(?P<poll_id>\d+)/$',views.detail,name='detail'),
    url(r'^(?P<poll_id>\d+)/result/$',views.result,name='result'),
    url(r'^(?P<poll_id>\d+)/vote/$',views.vote,name='vote'),
    '''
)
