# Generated by Django 3.2 on 2021-08-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210828_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='dob',
            field=models.DateField(auto_now_add=True),
        ),
    ]
