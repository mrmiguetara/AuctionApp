from django.db import models
from generics.models import BaseModel
from django.contrib.auth import get_user_model
from datetime import date, datetime
# Create your models here.
from django.utils.timezone import utc

def upload_image_to(instance, filename):
    return f'product/{instance.id}/{filename}'

class Category(BaseModel):
    name = models.CharField(max_length=50)

class Product(BaseModel):
    name = models.CharField(max_length=50)
    available_time = models.DateTimeField()
    details = models.TextField()
    short_description = models.CharField(max_length=20)
    minimum_bid = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    image = models.ImageField(upload_to=upload_image_to)

    categories = models.ManyToManyField(Category, related_name='products')

    @property
    def remaining_time(self):
        utc_now = datetime.utcnow()    

        d = utc.localize(utc_now)

        return self.available_time - d




class Bid(BaseModel):
    value = models.DecimalField(max_digits=12, decimal_places=0, default=0)

    user = models.ForeignKey(get_user_model(), related_name='bids', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='bids', on_delete=models.CASCADE)
    # auto_bid = models.BooleanField(default=False)


class Setting(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='settings')
    alert_percent = models.DecimalField(max_digits=3, decimal_places=0)
    total_reserved = models.DecimalField(max_digits=12, decimal_places=2)

    auto_bid_products = models.ManyToManyField(Product, related_name='settings')
