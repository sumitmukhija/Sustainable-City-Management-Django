from django.shortcuts import render, get_object_or_404
#from .models import PollutionDetails
#from .serializers import PollSerializer
from rest_framework import status
import json
from rest_framework.views import APIView
from rest_framework.response import Response
#from flask import Response
#from flask.wrappers import Response
from .pollution_data_interactions import PollutionDataInteractions
from .bike_data_interactions import BikeDataInteractions
import json
from mongo_auth.permissions import AuthenticatedOnly

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

    permission_classes = [AuthenticatedOnly]

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