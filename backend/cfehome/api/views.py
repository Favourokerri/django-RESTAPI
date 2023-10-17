from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body
    data = {}

    try:
        data = json.loads(body)
        print(data.keys())
    except:
        print("no body")
    return JsonResponse({"message": "hello mr frank"})

#start at 38.