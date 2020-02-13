from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from DataInteractions.pollution.pollution_data_interactions import PollutionDataInteractions
from DataInteractions.bike.bike_data_interactions import BikeDataInteractions
from DataInteractions.traffic.traffic_data_interactions import TrafficDataInteractions
from DataInteractions.busstops.busstop_data_interactions import BusStopDataInteractions
import json

class PollDetails(APIView):
    
    def post(self, request, format=None):
        data = request.data
        data = data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
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
        data = data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
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
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)

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
        #response = TrafficDataInteractions().get_all_objects()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)

class BusStopDetails(APIView):
    def post(self, request, format=None):
        data = request.data
        data = data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        #serializer = PollSerializer(data=data)
        try:
            x = BusStopDataInteractions().insert_busstop_data(data)
        except Exception as e:
            print(str(e))
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = BusStopDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)