from django.db import models
from generics.models import BaseModel
from django.contrib.auth import get_user_model
# Create your models here.

def upload_image_to(instance, filename):
    return f'product/{instance.name}/{filename}'

class Category(BaseModel):
    name = models.CharField(max_length=50)

class Product(BaseModel):
    name = models.CharField(max_length=50)
    available_time = models.DateTimeField()
    details = models.TextField()
    minimum_bid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    image = models.ImageField(upload_to=upload_image_to)

    categories = models.ManyToManyField(Category, related_name='products')



class Bid(BaseModel):
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    user = models.ForeignKey(get_user_model(), related_name='bids', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='bids', on_delete=models.CASCADE)


# class AutoBid(BaseModel):
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='auto_bid_setting')
#     alert_percent = models.DecimalField(max_digits=3, decimal_places=2)
#     total_reserved = models.DecimalField(max_digits=12, decimal_places=2)
#     auto_bid_products = models.