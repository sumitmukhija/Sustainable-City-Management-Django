from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from DataRetrieval.bike_analysis.bike_analysis_util import BikeAnalysisUtil
# Create your views here.

class BikeAnalysisModel(APIView):
    def get(self, request):
        stop = request.GET['stop']
        response = BikeAnalysisUtil.get_predictions(stop)
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)
        # response = BusStopDataInteractions().get_latest_by_lat_long()
        # responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        # return Response(response, status=responseStatus)