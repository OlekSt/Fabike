# Generated by Django 3.1.4 on 2021-02-04 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_orderlineitem_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='grand_total',
            new_name='final_total',
        ),
    ]
