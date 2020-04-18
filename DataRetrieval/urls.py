from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bikeprediction/$', views.BikeAnalysisModel.as_view()),
    url(r'pollutionprediction/$', views.PollutionAnalysisModel.as_view())
]
