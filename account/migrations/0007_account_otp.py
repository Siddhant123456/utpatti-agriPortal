# Generated by Django 3.2 on 2021-09-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210829_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='otp',
            field=models.CharField(blank=True, default=0, max_length=10),
        ),
    ]
