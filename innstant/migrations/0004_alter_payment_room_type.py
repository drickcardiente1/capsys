# Generated by Django 4.1 on 2023-04-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innstant', '0003_payment_room_floor_payment_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='room_type',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]