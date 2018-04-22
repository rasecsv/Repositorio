from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
	url(r'^user/$',views.UserList.as_view()),
	url(r'^user/(?P<pk>[0-9+])/$',views.UserDetail.as_view()),
	url(r'^person/$',views.PersonList.as_view()),
	url(r'^person/(?P<pk>[0-9+])/$',views.PersonList.as_view()),
	url(r'^question/$',views.QuestionList.as_view()),
	url(r'^question/(?P<pk>[0-9+])/$',views.QuestionDetail.as_view()),
	url(r'^tag/$',views.TagList.as_view()),
	url(r'^tag/(?P<pk>[0-9+])/$',views.TagDetail.as_view()),
	url(r'^questiontag/$',views.QuestionTagList.as_view()),
	url(r'^question/(?P<pk>[0-9+])/$',views.QuestionTagDetail.as_view()),
	url(r'^answer/$',views.AnswerList.as_view()),
	url(r'^answer/(?P<pk>[0-9+])/$',views.AnswerDetail.as_view()),
		
}
urlpatterns = format_suffix_patterns(urlpatterns)