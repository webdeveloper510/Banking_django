# Generated by Django 3.2.9 on 2021-12-09 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0014_merge_20211209_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignbank',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='localbank',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
    ]