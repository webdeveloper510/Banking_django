# Generated by Django 3.2.9 on 2021-12-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0006_auto_20211202_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='transanction',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
