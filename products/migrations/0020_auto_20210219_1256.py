# Generated by Django 3.1.4 on 2021-02-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20210219_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image02',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_url01',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]