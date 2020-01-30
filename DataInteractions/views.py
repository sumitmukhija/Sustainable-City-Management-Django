from django.shortcuts import render, get_object_or_404
from rest_framework import status
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .pollution_data_interactions import PollutionDataInteractions
from .bike_data_interactions import BikeDataInteractions
import json

class PollDetails(APIView):
    
    def post(self, request, format=None):
        data = request.data
        data = data['data']
        data = json.loads(data)
        #serializer = PollSerializer(data=data)
        try:
            x = PollutionDataInteractions().insert_poll_data(data)
        except Exception as e:
            print(str(e))
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = PollutionDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)

class DublinBikeDetails(APIView):
    def post(self, request, format=None):
        data = request.data
        print(data)
        data = data['data']
        print(data)
        data = json.loads(data)
        #serializer = PollSerializer(data=data)
        try:
            x = BikeDataInteractions().insert_bike_data(data)
        except Exception as e:
            print(str(e))
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = BikeDataInteractions().get_latest_by_lat_long()
        return Response(response, status=status.HTTP_200_OK)
