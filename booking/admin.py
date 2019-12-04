from django.contrib import admin
from .models import Line, Station, Route, Neighbor

admin.site.register(Line)
admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Neighbor)
