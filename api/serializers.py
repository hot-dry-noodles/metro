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
