from django_filters import rest_framework as filters

from.models import *


# unsolved bug here casued by field_name. This class has not been used yet.
class LineFilter(filters.FilterSet):
    line_name = filters.CharFilter(field_name='line_name')

    class Meta:
        model = Route
        fields = ('line_name',)


class RouteFilter(filters.FilterSet):
    # begin = filters.CharFilter(field_name='begin')
    # end = filters.CharFilter(filed_name='end')

    class Meta:
        model = Route
        fields = ('begin', 'end')


