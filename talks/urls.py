from __future__ import absolute_import

 from django.conf.urls import patterns, url, include

 from . import views


 lists_patterns = patterns(
     '',
     url(r'^$', views.TalkListDetailView.as_view(), name='detail'),
 )

 urlpatterns = patterns(
     '',
     url(r'^lists/', include(lists_patterns, namespace='lists')),
 )
