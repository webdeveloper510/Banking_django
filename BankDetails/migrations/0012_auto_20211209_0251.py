# Generated by Django 3.2.9 on 2021-12-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0011_auto_20211209_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='completeddate',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='confirmdate',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]