# Generated by Django 3.2.9 on 2021-12-06 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0002_auto_20211204_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalance',
            name='Balance',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
