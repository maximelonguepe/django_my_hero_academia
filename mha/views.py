import json

from django.shortcuts import render
from django.http import HttpResponse
import requests
from mha.models import Agency


# Create your views here.


def index(request):
    url = "http://localhost:8080/agencies"
    result = requests.get(url)
    response = json.loads(result.text)
    agencies = []
    for responseUnique in response:
        agencies.append(Agency(**responseUnique))
    return HttpResponse("Hello World this is my first app")
