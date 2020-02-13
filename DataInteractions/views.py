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
from .pollution_data_interactions import PollutionDataInteractions
from .bike_data_interactions import BikeDataInteractions
import json
from mongo_auth.permissions import AuthenticatedOnly
from mongo_auth.utils import login_status

'''def pollution_detail(request, pk):
    #PollutionDetails.objects.create(index=1, timestamp=1573668514154, indexValue=12.2345)
    pollutiondetail = get_object_or_404(PollutionDetails, id=pk)
    return render(request, 'product_detail.html', {'PollutionDetails':pollutiondetail})'''


class PollDetails(APIView):

    permission_classes = [AuthenticatedOnly]

    def post(self, request, format=None):
        data = request.data
        print(data)
        data = data['data']
        print(data)
        data = json.loads(data)
        #serializer = PollSerializer(data=data)
        try:
            x = PollutionDataInteractions().insert_poll_data(data)
        except Exception as e:
            print(str(e))
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    '''def get(self, request):
        response = PollutionDataInteractions().get_all_objects()
        return Response(response, status=status.HTTP_200_OK)'''
    def get(self, request):
        response = PollutionDataInteractions().get_latest_by_lat_long()
        return Response(response, status=status.HTTP_200_OK)


class DublinBikeDetails(APIView):

    # permission_classes = [AuthenticatedOnly]
    permission_classes = [AuthenticatedOnly,BikeAuth]

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


class CheckAuthentication(APIView):

    # permission_classes = [AuthenticatedOnly]

    def get(self, request):
        try:
            ls = login_status(request)
            response = {
                "authorized":ls[0],
                "user":ls[1]
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            response = {
                "authorized": False,
                "user": None
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)