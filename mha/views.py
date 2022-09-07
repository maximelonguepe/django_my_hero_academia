import json

from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.template import loader

from mha.models import Agency


# Create your views here.


def index(request):
    url = "http://localhost:8080/agencies"
    result = requests.get(url)
    response = json.loads(result.text)
    agencies = []
    for responseUnique in response:
        agencies.append(Agency(**responseUnique))
    context = {
        'agencies': agencies,
    }

    return render(request, 'mha/index.html', context)


def agency_details(request, agency_id):
    response = "You're looking for the agency %s."
    return HttpResponse(response % agency_id)



