# Generated by Django 3.1.6 on 2021-02-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0008_auto_20210218_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, unique=True),
        ),
    ]
