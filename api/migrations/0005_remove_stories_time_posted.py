# Generated by Django 3.2.9 on 2022-10-11 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_stories_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stories',
            name='time_posted',
        ),
    ]