# Generated by Django 5.0.1 on 2024-01-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inntrack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='delivery_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='priority',
            field=models.IntegerField(),
        ),
    ]
