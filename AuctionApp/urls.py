"""AuctionApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.staticfiles.urls import static
from . import settings
from bids.views import HomeView, ProductView, SettingView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('products/<int:product_id>', ProductView.as_view(), name='product'),
    # path('products/<int:product_id>/bid', post_bid, name='bid'),
    path('settings/', SettingView.as_view(), name='settings')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
