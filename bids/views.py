from django.http.response import HttpResponse, JsonResponse
from django.views.generic import View, DetailView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import json
from bids.models import Product, Category, Bid, Setting
# Create your views here.


class BaseView(LoginRequiredMixin, View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context


class HomeView(BaseView, ListView):
    template_name = 'bids/home.html'
    model=Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()
        return context

class ProductView(BaseView, DetailView):
    template_name = 'bids/product.html'
    model = Product
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['products'] = Product.objects.all()
        context['bid'] = Bid.objects.filter(product=context['product']).last()
        setting = Setting.objects.get(user=self.request.user)
        context['auto_bid'] = setting.auto_bid_products.filter(pk=context['product'].pk)
        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        product = Product.objects.get(pk=data.get('product_id'))
        bid_value = data.get('bid_amount')
        # print(data, product, bid_value)

        Bid.objects.create(
            user=request.user,
            product=product,
            value=bid_value
        )

        settings = Setting.objects.filter(auto_bid_products=product).exclude(user=request.user)
        for setting in settings:
            biggest_bid = Bid.objects.filter(product=product).order_by('value').first()
            last_user_bid = Bid.objects.filter(product=product, user=setting.user).last()
            diff = biggest_bid.value - last_user_bid.value
            goal = float(diff) + 1.0
            if goal > setting.total_reserved:
                # Not enough funds
                continue

            bid_value = float(biggest_bid.value) + goal
            Bid.objects.create(
                user=setting.user,
                product=product,
                value=bid_value
            )
            setting.total_reserved = float(setting.total_reserved ) - goal
            setting.save()

        response = {'status': 1, 'message': ("Ok")}
        return JsonResponse(response, safe=False)


class SettingView(BaseView, ListView):
    model=Setting
    template_name='bids/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['products'] = Product.objects.all()
        context['setting'] = Setting.objects.get(user=self.request.user)
        return context

    def post(self, request, **kwargs):
        data = json.loads(request.body)

        alert_percent = data.get('alert_percent')
        total_reserved = data.get('total_reserved')

        if alert_percent < 1 and alert_percent > 100:
            return JsonResponse(
                {'status': 2, 'message': ("Not valid alert percent. ")}
            )

        setting = Setting.objects.get(user=request.user)
        setting.alert_percent = alert_percent
        setting.total_reserved = total_reserved

        setting.save()

        response = {'status': 1, 'message': ("Ok")}
        return JsonResponse(response, safe=False)