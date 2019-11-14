from django.shortcuts import render, get_object_or_404
from .models import PollutionDetails
from .serializers import PollSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

def pollution_detail(request, pk):
    #PollutionDetails.objects.create(index=1, timestamp=1573668514154, indexValue=12.2345)
    pollutiondetail = get_object_or_404(PollutionDetails, id=pk)
    return render(request, 'product_detail.html', {'PollutionDetails':pollutiondetail})

class PollDetails(APIView):
    def post(self, request, format=None):
        data = request.data
        print(data)
        serializer = PollSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            print('Valid')
            poll = PollutionDetails(**data)
            poll.save()
            response = serializer.data
            print(response)
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = PollSerializer(PollutionDetails.objects.all(), many=True)
        response = {"PollutionDetails": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

