from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)

class Vehicle(models.Model):
    type = models.CharField(
        max_length=200,
        choices=[('scooter','scooter'),('bike','bike')]
    )
    serial = models.CharField(max_length=100)
    
    def last_trip_start(self):
        return self.trip_set.order_by('-start_time').first() if self.trip_set.exists() else None
        
    def trip_count(self):
        return self.trip_set.count()

    def is_available(self):
        last_trip = self.trip_set.order_by('-start_time').first()
        return bool(last_trip.end_time)


class Trip(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)
    start_x = models.FloatField()
    start_y = models.FloatField()
    start_time = models.DateTimeField()
    end_x = models.FloatField(blank=True)
    end_y = models.FloatField(blank=True)
    end_time = models.DateTimeField(blank=True)
