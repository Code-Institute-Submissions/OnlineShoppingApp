# Generated by Django 3.1.3 on 2020-11-16 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orderlineitem_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
    ]
