from django_filters import rest_framework 
from booking.models import * 

class StationFilter(rest_framework.FilterSet):
    class Meta:
        model = Station
        fields = ('station_name',)


class LineFilter(rest_framework.FilterSet):
    class Meta:
        model = Line
        fields = ('line_name',)

class RouteFilter(rest_framework.FilterSet):
    class Meta:
        model = Route
        fields = ('begin', 'end',)

class NeighborFilter(rest_framework.FilterSet):
    class Meta:
        model = Neighbor
        fields = ('line', 'station',)