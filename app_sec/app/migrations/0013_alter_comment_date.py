# Generated by Django 4.0 on 2021-12-26 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_merge_0003_alter_comment_date_0011_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 17, 53, 18, 849744)),
        ),
    ]