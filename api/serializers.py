from django.contrib.auth.models import User, Group
from rest_framework import serializers
from booking.models import Station, Line, Route, Neighbor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
                    
                
class StationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Station
        fields = ['station_name']


class LineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Line
        fields = ['line_name']


class RouteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Route
        fields = ['begin', 'end', 'distance', 'route', 'price', 'time']


class NeighborSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Neighbor
        fields = ['line', 'next_station', 'station', 'prev_station']