# Generated by Django 4.1 on 2022-08-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_series_url_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='url_name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]