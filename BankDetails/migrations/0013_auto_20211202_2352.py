# Generated by Django 3.2.9 on 2021-12-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0012_remove_transanction_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transanction',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='userbalance',
            name='AccountNumber',
            field=models.FloatField(default=0),
        ),
    ]