from django.contrib import admin
from bids.models import Category, Product, Bid, Setting
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Bid)
admin.site.register(Setting)