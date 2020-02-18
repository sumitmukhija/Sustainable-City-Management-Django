from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
#from flask import Response
#from flask.wrappers import Response
from DataInteractions.auth import *
from DataInteractions.pollution.pollution_data_interactions import PollutionDataInteractions
from DataInteractions.bike.bike_data_interactions import BikeDataInteractions
from DataInteractions.traffic.traffic_data_interactions import TrafficDataInteractions
import json
from mongo_auth.permissions import AuthenticatedOnly
from mongo_auth.utils import login_status

class PollDetails(APIView):
    
    permission_classes = [AuthenticatedOnly]
    
    def post(self, request, format=None):
        data = request.data
        data = data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = PollutionDataInteractions().insert_poll_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = PollutionDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)


class DublinBikeDetails(APIView):

    permission_classes = [AuthenticatedOnly,BikeAuth]

    def post(self, request, format=None):
        data = request.data
        data = data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = BikeDataInteractions().insert_bike_data(data)
        except Exception as e:
            return Response(
              
              
              x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = BikeDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)

class CheckAuthentication(APIView):

    def get(self, request):
        try:
            flag, user_obj = login_status(request)
            response = {
                "authorized":flag,
                "user":user_obj
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                "authorized": False,
                "user": None
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class TrafficDetails(APIView):
    def post(self, request, format=None):
        data = request.data
        data = data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = TrafficDataInteractions().insert_traffic_data(data)
        except Exception as e:
            print(str(e))
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = TrafficDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)
