# Generated by Django 4.0.5 on 2022-08-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_voucher_rateper'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='party_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
