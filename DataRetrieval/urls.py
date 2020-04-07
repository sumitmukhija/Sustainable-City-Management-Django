from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.home, name='test-data-retrieval-home'),
    url(r'bikeprediction/$', views.BikeAnalysisModel.as_view())
]
