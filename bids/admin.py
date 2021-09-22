from django.contrib import admin
from bids.models import Category, Product, Bid
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Bid)