# Generated by Django 3.1.6 on 2021-02-18 14:45

from django.db import migrations, models
import geolocation.validator


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0005_auto_20210215_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='url_address',
            field=models.CharField(max_length=255, null=True, validators=[geolocation.validator.validate_urn]),
        ),
    ]
