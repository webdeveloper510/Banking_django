# Generated by Django 3.2.9 on 2021-12-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0013_auto_20211202_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transanction',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('completed', 'completed')], max_length=200, unique=True),
        ),
    ]
