# Generated by Django 2.0 on 2017-12-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_auto_20171215_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
