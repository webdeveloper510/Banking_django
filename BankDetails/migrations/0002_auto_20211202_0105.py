# Generated by Django 3.2.9 on 2021-12-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foreignbank',
            name='username',
        ),
        migrations.AddField(
            model_name='localbank',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
