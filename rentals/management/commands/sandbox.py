from django.core.management import BaseCommand
from rentals.models import User, Vehicle, Trip


"""
Uncomment some of the content here to experiment with prefetch_related and select_related behavior.
Modify django logging settings if you want to see database calls.
You'll want to populate the database with some data beforehand.

Usage: python manage.py sandbox
"""

class Command(BaseCommand):
    """
    Observe differences in query behavior between prefetch_related, select_related, or none
    """

    help = "testing"

    def handle(self, *args, **options):
        trips = Trip.objects.all()

        result = trips.filter(vehicle__type='scooter')[:50]
        # result = trips.filter(vehicle__type='scooter')[:50].prefetch_related('vehicle')
        # result = trips.filter(vehicle__type='scooter')[:50].select_related('vehicle')

        # print(result)

        for trip in result:
            print(trip, trip.vehicle.type)


# class Command(BaseCommand):
#     """
#     Depending on the cardinality of the database object relationship, select_related may not be usable.
#     """

#     help = "testing"

#     def handle(self, *args, **options):
#         # vehicles = Vehicle.objects.all().select_related('trip_set')  # won't work
#         vehicles = Vehicle.objects.all().prefetch_related('trip_set')

#         for vehicle in vehicles:
#             print(vehicle, vehicle.trip_set.count())
