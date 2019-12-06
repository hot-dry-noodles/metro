from django.db import models

max_name_length = 256
max_time_text_length = 8
max_route_text_length = 4096


class Line(models.Model):
    line_name = models.CharField(max_length=max_name_length, default = '')


class Station(models.Model):
    station_name = models.CharField(max_length=max_name_length, default = '')
    first_working = models.CharField(max_length=max_time_text_length, default = '')
    last_working = models.CharField(max_length=max_time_text_length, default = '')
    first_off = models.CharField(max_length=max_time_text_length, default = '')
    last_off = models.CharField(max_length=max_time_text_length, default = '')


class Route(models.Model):
    begin = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='begin_station')
    end = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='end_station')
    distance = models.FloatField(default=float('inf'))
    route = models.CharField(max_length=max_route_text_length)
    price = models.IntegerField(default=0)


class Neighbor(models.Model):
    station = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='neighbor_station')
    line = models.ForeignKey(
        Line, on_delete=models.DO_NOTHING, related_name='neighbor_line')
    prev_station = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='neighbor_prev_station')
    next_station = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='neighbor_next_station')
