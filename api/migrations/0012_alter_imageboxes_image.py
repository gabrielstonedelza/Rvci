# Generated by Django 3.2.9 on 2021-12-13 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20211213_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageboxes',
            name='image',
            field=models.TextField(),
        ),
    ]