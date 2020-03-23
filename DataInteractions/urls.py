from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'polls', views.PollDetails.as_view()),
    url(r'bike', views.DublinBikeDetails.as_view()),
    url(r'user', views.CheckAuthentication.as_view()),
    url(r'traffic/analysis', views.TrafficAnalysisDetails.as_view()),
    url(r'traffic', views.TrafficDetails.as_view()),
    url(r'busstop', views.BusStopDetails.as_view()),
    url(r'luasstop', views.LuasStopDetails.as_view()),
    url(r'irishrailstop', views.IrishRailStopDetails.as_view()),
    url(r'notify', views.NotificationDispatch.as_view()),
]
