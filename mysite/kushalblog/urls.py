from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from kushalblog.models import Post

urlpatterns = patterns ('',
							url(r'^$', ListView.as_view(
								queryset = Post.objects.all().order_by("-date")[:10],
								template_name = "kushalblog.html")),


							url(r'^(?P<pk>\d+)$', DetailView.as_view(
								model = Post,
								template_name = "post.html")),

							url(r'^archives/$', ListView.as_view(
								queryset = Post.objects.all().order_by("-date"),
								template_name = "posttitlelist.html")),

							url(r'^latestnews/$', ListView.as_view(
								queryset = Post.objects.all().order_by("-date")[:2],
								template_name = "posttitlelist.html")),

	)