# Generated by Django 3.2.7 on 2021-09-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0002_auto_20210924_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
