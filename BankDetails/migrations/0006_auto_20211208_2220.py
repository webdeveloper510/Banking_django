# Generated by Django 3.2.9 on 2021-12-08 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0005_transaction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='Date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('completed', 'completed')], default='pending', max_length=200),
        ),
    ]