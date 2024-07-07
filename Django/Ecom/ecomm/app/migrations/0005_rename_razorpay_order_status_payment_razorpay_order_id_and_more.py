# Generated by Django 5.0.6 on 2024-07-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_payment_orderplaced'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_order_status',
            new_name='razorpay_order_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_payment_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]