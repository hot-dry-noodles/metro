from django.contrib import admin
from .models import Line, Terminal, Route, Neighbor

admin.site.register(Line)
admin.site.register(Terminal)
admin.site.register(Route)
admin.site.register(Neighbor)
