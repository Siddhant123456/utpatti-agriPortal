# Generated by Django 3.2 on 2021-08-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile',
            field=models.CharField(default='merchant', max_length=20),
        ),
    ]
