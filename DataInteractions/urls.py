from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'polls', views.PollDetails.as_view()),
    url(r'bike', views.DublinBikeDetails.as_view()),
    url(r'traffic', views.TrafficDetails.as_view()),
    url(r'busstop', views.BusStopDetails.as_view()),
    url(r'luasstop', views.LuasStopDetails.as_view()),
]