# Generated by Django 3.2.9 on 2022-01-09 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_dailyvids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='date_posted',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stories',
            name='time_posted',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
