# Generated by Django 3.2.9 on 2021-12-02 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0011_transanction_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transanction',
            name='amount',
        ),
    ]