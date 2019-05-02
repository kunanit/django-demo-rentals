from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from . import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'trips', views.TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test', views.test_view),
    path('test_api', views.test_api_view),
    path('test_template', views.test_template_view),
    path('schema', views.schema_view),
    path('docs/', include_docs_urls(title='Rentals API')),
]
