from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from bids.models import Category, Product, Setting

from django.core.files import File  # you need this somewhere
import urllib

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        self.stdout.write('Creating users...')
        
        user_1 = User.objects.create_user('user_1', 'user_1@auction_scopic.com', 'p@ssw0rd')
        user_2 = User.objects.create_user('user_2', 'user_2@auction_scopic.com', 'p@ssw0rd')

        self.stdout.write('Creating settings')

        Setting.objects.create(user=user_1, alert_percent=90, total_reserved=1000)
        Setting.objects.create(user=user_2, alert_percent=90, total_reserved=1000)

        self.stdout.write('Creating Products and categories')

        vehicles = Category.objects.create(name='Vehicles')
        antiques = Category.objects.create(name='Antiques')
        art = Category.objects.create(name='Art')

        p1 = Product()
        p1.name = 'Toyota Corolla 2002'
        p1.available_time = datetime.now() + timedelta(hours=4)
        p1.details = 'Excelent vehicle. Passed from generation through generation'
        p1.short_description = 'A very old car'
        p1.minimum_bid = 4000

        p1.save()
        p1.image = '/product/1/car.jpeg'
        p1.save()

        p1.categories.add(vehicles)

        p2 = Product()
        p2.name = 'Katana sword'
        p2.available_time = datetime.now() + timedelta(hours=4)
        p2.details = 'Excelent katana. Passed from generation through generation'
        p2.short_description = 'A very old katana'
        p2.minimum_bid = 8000
        p2.save()

        p2.image = '/product/2/katana.jpg'
        p2.save()
        p2.categories.add(antiques)

        p3 = Product()
        p3.name = 'Painting'
        p3.available_time = datetime.now() + timedelta(hours=4)
        p3.details = 'Excelent painting. Passed from generation through generation'
        p3.short_description = 'A very old painting'
        p3.minimum_bid = 2000
        p3.save()
        p3.image = '/product/3/painting.jpg'

        p3.categories.add(art)

        p1.save()
        p2.save()
        p3.save()

        self.stdout.write('Seed finish.')
