# Generated by Django 4.1 on 2022-08-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_newuser_passwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
