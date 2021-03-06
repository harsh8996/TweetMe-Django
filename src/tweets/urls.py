from django.conf.urls import url
from .views  import tweet_detail_view,tweet_list_view,TweetDetailView,TweetListView,TweetCreateView,TweetUpdateView,TweetDeleteView

urlpatterns = [
    # url(r'^$', tweet_list_view,name='list'),
    # url(r'^(?P<id>\d+)/$', tweet_detail_view,name='detail'),

    url(r'^$', TweetListView.as_view(),name='list'),
    url(r'^create/$', TweetCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(),name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(),name='delete'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(),name='detail'),
]

