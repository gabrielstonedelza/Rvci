# Generated by Django 3.2.9 on 2021-12-28 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_stories_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='time_posted',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
