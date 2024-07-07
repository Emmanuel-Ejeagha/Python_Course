# Generated by Django 5.0.6 on 2024-07-06 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_razorpay_order_status_payment_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_order_id',
            new_name='stripe_order_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_id',
            new_name='stripe_payment_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_status',
            new_name='stripe_payment_status',
        ),
    ]
