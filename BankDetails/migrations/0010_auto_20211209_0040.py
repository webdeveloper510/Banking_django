# Generated by Django 3.2.9 on 2021-12-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0009_auto_20211208_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='completeddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='confirmdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(),
        ),
    ]
