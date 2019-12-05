from django.contrib.auth.models import User, Group
from rest_framework import serializers
from booking.models import Station, Line, Route


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
        fields = ['name']


class LineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Line
        fields = ['line_name', 'station_name', 'first_working',
                  'last_working', 'first_off', 'last_off']


class RouteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Route
        fields = ['begin', 'end', 'distance', 'price', 'route']