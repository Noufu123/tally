# Generated by Django 4.0.5 on 2022-07-29 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_stock_item_delete_stock_item_crt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock_item',
            old_name='per',
            new_name='rateper',
        ),
        migrations.RemoveField(
            model_name='stock_item',
            name='rate',
        ),
    ]
