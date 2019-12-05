from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, StationSerializer
from booking.models import Station, Line, Route
from .serializers import UserSerializer, GroupSerializer, StationSerializer, RouteSerializer, LineSerializer
from booking.models import Station, Line, Route
from django_filters import rest_framework
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


class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lines to be viewed or edited.
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ('line_name')


class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows routes to be viewed or edited.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ('begin', 'end')

def findRoute(request, bstation_name, estation_name):
    """
    Find the route with two stations.
    """
    bstation = Station.objects.filter(station_name = bstation_name).first()
    estation = Station.objects.filter(station_name = estation_name).first()
    chosen_route = Route.objects.filter(begin_id = bstation.id, end_id = estation.id).first()
    
    # render ...

def findStationInLine(request, _line_name):
    """
    Find all stations in a line in order
    """
    chosen_line = Line.objects.filter(line_name = _line_name).first()
    station_list = Line.objects.filter(line_id = chosen_line.id).order_by('id')

    # render ...