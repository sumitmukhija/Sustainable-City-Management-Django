from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='test-data-retrieval-home'),
]
