# Generated by Django 3.1.4 on 2021-02-12 09:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('topics', models.TextField(max_length=240)),
                ('learning', models.TextField(max_length=240)),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=80)),
                ('address_line', models.CharField(max_length=60)),
                ('town_or_city', models.CharField(max_length=50)),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('comment', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
