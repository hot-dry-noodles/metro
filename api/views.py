from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, StationSerializer, RouteSerializer, LineSerializer, NeighborSerializer
from .filters import RouteFilter
from booking.models import Station, Line, Route, Neighbor
from django_filters import rest_framework
import re
# from booking.filters import RouteFilter
# from booking.filters import LineFilter

def convert(s):
    if len(s) != 1:
        temp = re.findall(r'[0-9]+|[a-z]+', s)
        str = ''
        for i in iter(temp):
            if i.isdigit():
                i = int(i)
                station = Station.objects.get(id=i+1).station_name
                str = str + station.__str__() + ' '
            else:
                i = ord(i) - ord('a') + 1
                line = Line.objects.get(id=i).line_name
                str = str + line.__str__() + ' '

    return str.rstrip()

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
    # filter_class = StationFilter


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

    def get_queryset(self):
        queryset = Route.objects.all()
        begin_station = self.request.query_params.get('begin', None)
        end_station = self.request.query_params.get('end', None)
        begin_id = Station.objects.filter(station_name=begin_station).first()
        end_id = Station.objects.filter(station_name=end_station).first()
        queryset = queryset.filter(begin=begin_id).filter(end=end_id)

        entry = queryset.get(begin=begin_id, end=end_id)
        entry.route = convert(entry.route.__str__())
        for query in queryset:
            query.route = entry.route
        return queryset
        # queryset = Route.objects.all()

    serializer_class = RouteSerializer


    # filter_backends = (rest_framework.DjangoFilterBackend,)
    # filter_fields = ('begin', 'end')
    #filter_backends = (rest_framework.DjangoFilterBackend,)
    # filter_class = RouteFilter


class NeighborViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows neighbors to be viewed or edited.
    """
    queryset = Neighbor.objects.all()
    serializer_class = NeighborSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)

    # filter_class = NeighborFilter

# NOT FINISHED YET
# EACH QUERY MAPS A NEED

# def findRoute(request, bstation_name, estation_name):
#     """
#     Find the distacne, route, price with two stations.
#     """
#
#     if request.method == 'GET':
#
#         try:
#             bstation = Station.objects.filter(station_name = bstation_name).first()
#             estation = Station.objects.filter(station_name = estation_name).first()
#             chosen_route = Route.objects.filter(begin = bstation.station_name, end = estation.station_name).first()
#         except:
#             # return HttpResponse(status=404)
#
#         serializer = RouteSerializer(chosen_route)
#         serializer_data = serializer.data
#
#         del serializer_data['begin']
#         del serializer_data['end']
#
#         # return HttpResponse(json.dumps(serializer_data, ensure_ascii=False),
#         #                         content_type="application/json, charset=utf-8")
#
#
# def findStationInLine(request, _line_name):
#     """
#     Find all stations in a line in order.
#     """
#
#     if request.method == 'GET':
#
#         try:
#             station_list = Neighbor.objects.filter(line=_line_name).order_by('id')
#         except:
#             return HttpResponse(status=404)
      
        # serializer = NeighborSerializer(station_list)
        # serializer_data = serializer.data
        #
        # for i in iter(serializer_data):
        #     del serializer_data[i]['line']
        #     del serializer_data[i]['prev_station']
        #     del serializer_data[i]['next_station']
        
        # return HttpResponse(json.dumps(serializer_data, ensure_ascii=False),
        #                         content_type="application/json, charset=utf-8")




