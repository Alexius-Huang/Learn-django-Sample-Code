from django.conf.urls import url
from .                import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<question_id>[0-9]+)/$',         views.detail,  name = 'detail'),    # Ex : /polls/5/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = 'results'),   # Ex : /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/vote/$',    views.vote,    name = 'vote'),      # Ex : /polls/5/vote/
]