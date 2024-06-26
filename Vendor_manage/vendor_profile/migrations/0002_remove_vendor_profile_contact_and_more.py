# Generated by Django 5.0 on 2024-04-29 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor_profile',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='vendor_profile',
            name='on_time_delivery',
        ),
        migrations.AddField(
            model_name='vendor_profile',
            name='contact_details',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor_profile',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor_profile',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vendor_profile',
            name='average_response_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor_profile',
            name='fulfillment_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor_profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor_profile',
            name='quality_rating_avg',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendor_profile',
            name='vendor_code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
