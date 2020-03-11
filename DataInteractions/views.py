from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
#from flask import Response
#from flask.wrappers import Response
from DataInteractions.auth import *
from DataInteractions.pollution.pollution_data_interactions import PollutionDataInteractions
from DataInteractions.bike.bike_data_interactions import BikeDataInteractions
from DataInteractions.traffic.traffic_data_interactions import TrafficDataInteractions
from DataInteractions.busstops.busstop_data_interactions import BusStopDataInteractions
from DataInteractions.luasstops.luasstop_data_interactions import LuasStopDataInteractions
from DataInteractions.irishrail.irishrailstop_data_interactions import IrishRailStopDataInteractions
from DataInteractions.alerts.alerts_data_interactions import AlertsDataInteractions
import json
from mongo_auth.permissions import AuthenticatedOnly
from mongo_auth.utils import login_status
from django.core.cache import cache


class PollDetails(APIView):
    
    permission_classes = [AuthenticatedOnly]
    
    def post(self, request, format=None):
        data = request.data['data']
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
        data = request.data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = BikeDataInteractions().insert_bike_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
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

class TrafficAnalysisDetails(APIView):
    
    permission_classes = [AuthenticatedOnly]

    def post(self, request, format=None):
        data = request.data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = TrafficDataInteractions().insert_traffic_analysis_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = TrafficDataInteractions().get_latest_analysis_data_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)



class TrafficDetails(APIView):

    permission_classes = [AuthenticatedOnly]

    def post(self, request, format=None):
        data = request.data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = TrafficDataInteractions().insert_traffic_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = TrafficDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)


class BusStopDetails(APIView):

    permission_classes = [AuthenticatedOnly, BusAuth]

    def post(self, request, format=None):
        data = request.data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = BusStopDataInteractions().insert_busstop_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = BusStopDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)


class LuasStopDetails(APIView):

    permission_classes = [AuthenticatedOnly, LuasAuth]

    def post(self, request, format=None):
        data = request.data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = LuasStopDataInteractions().insert_luasstop_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = LuasStopDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)

class IrishRailStopDetails(APIView):
    
    permission_classes = [AuthenticatedOnly, DartAuth]

    def post(self, request, format=None):
        data = request.data['data']
        if data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(data)
        try:
            x = IrishRailStopDataInteractions().insert_irishrailstop_data(data)
        except Exception as e:
            return Response(str(x), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = IrishRailStopDataInteractions().get_latest_by_lat_long()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)

class FlagDetails(APIView):

    permission_classes = [AuthenticatedOnly]

    def post(self, request, format=None):
        print(request.data)
        if request.data is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        try:
           x =  cache.set("isAlertPresent", request.data["isAlertPresent"], timeout=None)
        except Exception as e:
            return Response('Exception', status=status.HTTP_400_BAD_REQUEST)
        return Response('Success', status=status.HTTP_201_CREATED)
    
    def get(self, request):
        return Response({'isAlertPresent': cache.get("isAlertPresent")}, status=status.HTTP_200_OK)

class AlertList(APIView):
    def post(self, request, format=None):
        data = request.data
        if request is None:
            return Response("No Data", status=status.HTTP_400_BAD_REQUEST)
        # data = json.loads(data)
        try:
            x = AlertsDataInteractions().update_alert(data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(str(x), status=status.HTTP_201_CREATED)

    def get(self, request):
        response = AlertsDataInteractions().get_alerts()
        responseStatus = status.HTTP_200_OK if response is not None else status.HTTP_404_NOT_FOUND
        return Response(response, status=responseStatus)