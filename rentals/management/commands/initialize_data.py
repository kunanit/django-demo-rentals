from django.core.management import BaseCommand
import pandas as pd
from rentals.models import User, Vehicle, Trip


class Command(BaseCommand):
    help = "Load trip data"

    def handle(self, *args, **options):
        # clean up previous data
        Trip.objects.all().delete()
        User.objects.all().delete()
        Vehicle.objects.all().delete()

        df_users = pd.read_csv('/app/data/sample_users.csv')[['username']]
        df_vehicles = pd.read_csv('/app/data/sample_vehicles.csv')[['serial', 'type']]
        df_trips = pd.read_csv('/app/data/sample_trips.csv')
                
        User.objects.bulk_create([User(**row) for row in df_users.to_dict('records')])
        Vehicle.objects.bulk_create([Vehicle(**row) for row in df_vehicles.to_dict('records')])

        users = {u.username: u for u in User.objects.all()}
        vehicles = {v.serial: v for v in Vehicle.objects.all()}

        def generate_trip_obj(row):
            user = users[row.pop('user_username')]
            vehicle = vehicles[row.pop('vehicle_serial')]
            return Trip(user=user, vehicle=vehicle, **row)

        Trip.objects.bulk_create(generate_trip_obj(row) for row in df_trips.to_dict('records'))
        
        print(f'{User.objects.count()} users created')
        print(f'{Vehicle.objects.count()} vehicles created')
        print(f'{Trip.objects.count()} trips created')
