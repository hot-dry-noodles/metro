from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'stations', views.StationViewSet)
<<<<<<< HEAD
=======
router.register(r'lines', views.LineViewSet)
router.register(r'routes', views.RouteViewSet)
>>>>>>> 94c587dc87862e0bf19664e34b0024ddfab731df

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls', namespace='rest_framework'))
]
