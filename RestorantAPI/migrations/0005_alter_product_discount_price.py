# Generated by Django 3.2.11 on 2022-02-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestorantAPI', '0004_auto_20220210_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]
