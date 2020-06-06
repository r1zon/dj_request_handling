import csv
from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from app import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    results = []
    url = 'bus_stations'
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            results.append(row)
    current_page = int(request.GET.get('page', 1))
    if current_page*10 > len(results):
        current_page = round(len(results)/10)
    next_page_url = '?'.join((url, urlencode({'page': current_page+1})))
    prev_page_url = '?'.join((url, urlencode({'page': current_page-1})))
    bus_stations = []
    for i in range((current_page-1)*10,current_page*10):
        bus_stations.append({'Name': results[i]['Name'], 'Street': results[i]['Street'], 'District': results[i]['District']})
    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

