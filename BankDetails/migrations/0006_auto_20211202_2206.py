# Generated by Django 3.2.9 on 2021-12-02 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BankDetails', '0005_alter_userbalance_accountnumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbalance',
            old_name='BankId',
            new_name='BankID',
        ),
        migrations.RenameField(
            model_name='userbalance',
            old_name='UserID',
            new_name='UserId',
        ),
        migrations.AlterField(
            model_name='localbank',
            name='Accountnumber',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='localbank',
            name='rountingnumber',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='userbalance',
            name='AccountNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Accountnumber', to='BankDetails.userprofile'),
        ),
    ]
