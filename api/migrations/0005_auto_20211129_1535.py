# Generated by Django 3.2.9 on 2021-11-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211125_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stories',
            name='time_posted',
        ),
        migrations.AlterField(
            model_name='stories',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
