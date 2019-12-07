import json
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django_filters import rest_framework
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .serializers import *
from .filters import *
from booking.models import * 
# from booking.filters import RouteFilter
# from booking.filters import LineFilter


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stations to be viewed or edited.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = StationFilter

class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lines to be viewed or edited.
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = LineFilter


class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows routes to be viewed or edited.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = RouteFilter 

class NeighborViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows neighbors to be viewed or edited.
    """
    queryset = Neighbor.objects.all()
    serializer_class = NeighborSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = NeighborFilter   

# NOT FINISHED YET
# EACH QUERY MAPS A NEED

def findRoute(request, bstation_name, estation_name):
    """
    Find the distacne, route, price with two stations.
    """
    
    if request.method == 'GET':
        
        try: 
            bstation = Station.objects.filter(station_name = bstation_name).first()
            estation = Station.objects.filter(station_name = estation_name).first()
            chosen_route = Route.objects.filter(begin = bstation.station_name, end = estation.station_name).first()
        except:
            return HttpResponse(status=404)

        serializer = RouteSerializer(chosen_route)
        serializer_data = serializer.data
        
        del serializer_data['begin']
        del serializer_data['end']

        return HttpResponse(json.dumps(serializer_data, ensure_ascii=False), 
                                content_type="application/json, charset=utf-8")


def findStationInLine(request, _line_name):
    """
    Find all stations in a line in order.
    """
    
    if request.method == 'GET':
        
        try:
            station_list = Neighbor.objects.filter(line=_line_name).order_by('id')
        except:
            return HttpResponse(status=404)
      
        serializer = NeighborSerializer(station_list)
        serializer_data = serializer.data

        for i in iter(serializer_data):
            del serializer_data[i]['line']
            del serializer_data[i]['prev_station']
            del serializer_data[i]['next_station']
        
        return HttpResponse(json.dumps(serializer_data, ensure_ascii=False), 
                                content_type="application/json, charset=utf-8")




