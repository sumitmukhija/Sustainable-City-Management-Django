from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'polls', views.PollDetails.as_view()),
    url(r'bike', views.DublinBikeDetails.as_view()),
    url(r'user', views.CheckAuthentication.as_view()),
]