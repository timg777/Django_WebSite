# Generated by Django 3.0.1 on 2020-01-04 08:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_sportnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 4, 8, 37, 47, 637458, tzinfo=utc)),
        ),
    ]