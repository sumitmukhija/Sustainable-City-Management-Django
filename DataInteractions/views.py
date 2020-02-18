from django.shortcuts import render, get_object_or_404
#from .models import PollutionDetails
#from .serializers import PollSerializer
from rest_framework import status
import json
from rest_framework.views import APIView
from rest_framework.response import Response
#from flask import Response
#from flask.wrappers import Response
from DataInteractions.auth import *
from DataInteractions.pollution_data_interactions import PollutionDataInteractions
from DataInteractions.bike_data_interactions import BikeDataInteractions
import json
from mongo_auth.permissions import AuthenticatedOnly
from mongo_auth.utils import login_status


class PollDetails(APIView):

    permission_classes = [AuthenticatedOnly]

    def post(self, request, format=None):
        data = request.data
        data = data['data']
        data = json.loads(data)
        #serializer = PollSerializer(data=data)
        try:
            x = PollutionDataInteractions().insert_poll_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    '''def get(self, request):
        response = PollutionDataInteractions().get_all_objects()
        return Response(response, status=status.HTTP_200_OK)'''
    def get(self, request):
        response = PollutionDataInteractions().get_latest_by_lat_long()
        return Response(response, status=status.HTTP_200_OK)


class DublinBikeDetails(APIView):

    permission_classes = [AuthenticatedOnly,BikeAuth]

    def post(self, request, format=None):
        data = request.data
        data = data['data']
        data = json.loads(data)
        #serializer = PollSerializer(data=data)
        try:
            x = BikeDataInteractions().insert_bike_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = BikeDataInteractions().get_latest_by_lat_long()
        return Response(response, status=status.HTTP_200_OK)


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