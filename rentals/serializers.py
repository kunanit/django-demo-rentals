from rest_framework import serializers
from .models import User, Vehicle, Trip


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'type']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']
    
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'id', 'user', 'vehicle', 'start_x','start_y',
            'end_x','end_y','start_time','end_time'
        ]
