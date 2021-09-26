from django import forms

class BidForm(forms.Form):
    product_id = forms.IntegerField()
    bid_value = forms.DecimalField()
    set_auto_bid = forms.BooleanField()

class SettingsForm(forms.Form):
    alert_percent = forms.IntegerField(min_value=1, max_value=100)
    total_reserved = forms.DecimalField()