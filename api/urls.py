from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'lines', views.LineViewSet)
router.register(r'routes', views.RouteViewSet)
router.register(r'neighbors', views.NeighborViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls', namespace='rest_framework'))
]
