# Generated by Django 4.0.5 on 2022-08-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_stock_item_rateper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_item',
            name='quantity',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voucherlist',
            name='rateper',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]