# Generated by Django 3.2 on 2021-08-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_farmerprofile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='aadhar_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]