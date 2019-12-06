from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django_filters import rest_framework
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
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
    Find the route with two stations.
    """
    bstation = Station.objects.filter(station_name = bstation_name).first()
    estation = Station.objects.filter(station_name = estation_name).first()
    chosen_route = Route.objects.filter(begin_id = bstation.id, end_id = estation.id).first()
    

def findStationInLine(request, _line_name):
    """
    Find all stations in a line in order
    """
    chosen_line = Line.objects.filter(line_name = _line_name).first()
    station_list = Line.objects.filter(line_id = chosen_line.id).order_by('id')

