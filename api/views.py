from django.contrib.auth.models import User, Group
from rest_framework import viewsets
<<<<<<< HEAD
from .serializers import UserSerializer, GroupSerializer, StationSerializer
from booking.models import Station, Line, Route
=======
from .serializers import UserSerializer, GroupSerializer, StationSerializer, RouteSerializer, LineSerializer
from booking.models import Station, Line, Route
from django_filters import rest_framework
# from booking.filters import RouteFilter
# from booking.filters import LineFilter
>>>>>>> 94c587dc87862e0bf19664e34b0024ddfab731df


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
<<<<<<< HEAD
=======


class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lines to be viewed or edited.
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ('line_name',)


class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows routes to be viewed or edited.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = ('begin', 'end')

    # filter_class = RouteFilter (unsolved bug here,
    # __init__ () conflicts with field_name in /booking/filters.py)
>>>>>>> 94c587dc87862e0bf19664e34b0024ddfab731df
