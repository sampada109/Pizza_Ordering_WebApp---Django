# Generated by Django 5.0.6 on 2024-07-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_customerorder_payment_request_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='total_amount',
            field=models.IntegerField(null=True),
        ),
    ]
