import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, renderers, schemas
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view, renderer_classes
from .models import User, Vehicle, Trip
from .serializers import UserSerializer, VehicleSerializer, TripSerializer
from rest_framework.schemas import get_schema_view


def test_view(request):
    print(request)
    return HttpResponse('hi there')


def test_api_view(request):
    vehicle = Vehicle.objects.get(id=1)
    return HttpResponse(json.dumps({'id':vehicle.id, 'type':vehicle.type}), content_type='application/json')


def test_template_view(request):
    trip_list = Trip.objects.order_by('-start_time')[:5]
    context = {'trip_list': trip_list}
    return render(request, 'rentals/example.html', context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @action(detail=True)
    def trip_count(self, request, *args, **kwargs):
        vehicle = self.get_object()
        return Response({'trip_count':vehicle.trip_count()})

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


schema_view = get_schema_view(title='My api schema')
