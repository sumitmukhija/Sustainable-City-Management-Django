from django.shortcuts import render
from django.http import JsonResponse
import datetime

# Create your views here.
def home(request):
    test_dictionary = {"message": "It's working!",
                       "time": datetime.datetime.now()}
    return JsonResponse(test_dictionary)
