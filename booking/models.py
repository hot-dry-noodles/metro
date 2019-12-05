from django.db import models

max_name_length = 256
max_time_text_length = 8
max_route_text_length = 4096


class Line(models.Model):
    line_name = models.CharField(max_length=max_name_length)
    station_name = models.CharField(max_length=max_name_length)
    first_working = models.CharField(max_length=max_time_text_length)
    last_working = models.CharField(max_length=max_time_text_length)
    first_off = models.CharField(max_length=max_time_text_length)
    last_off = models.CharField(max_length=max_time_text_length)


class Station(models.Model):
    name = models.CharField(max_length=max_name_length)


class Route(models.Model):
    begin = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='begin')
    end = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='end')
    distance = models.FloatField(default=float('inf'))
    price = models.IntegerField(default=0)
    route = models.CharField(max_length=max_route_text_length)


class Neighbor(models.Model):
    station = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='station')
    line = models.ForeignKey(Line, on_delete=models.DO_NOTHING)
    prev = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='prev')
    next = models.ForeignKey(
        Station, on_delete=models.DO_NOTHING, related_name='next')
