# Generated by Django 3.2.9 on 2021-12-08 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0004_alter_transaction_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
