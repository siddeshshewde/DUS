# Generated by Django 3.1 on 2020-10-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20201010_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorten_urls',
            name='visits',
            field=models.IntegerField(default=0),
        ),
    ]