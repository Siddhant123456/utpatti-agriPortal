# Generated by Django 3.2 on 2021-08-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_farmerprofile_aadhar_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='aadhar_number',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(auto_now_add=True),
        ),
    ]
