import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from CrimeDataSan.models import CrimeDate, CrimePosition

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        CrimeDate.objects.all().delete()
        CrimePosition.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/CrimeDataSan/DataSource_crime/crime.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:

                CrimeDateRows = CrimeDate.objects.create(
                date = row[0],
                weekday = row[1],
                district = row[2],
                address = row[3],
                )
                CrimeDateRows.save()

                CrimePositionRows = CrimePosition.objects.create(
                district = row[2],
                address = row[3],
                date = row[0],
                longitude = row[4],
                latitude = row[5],
                )
                CrimePositionRows.save()
        print("data parsed successfully")