# Generated by Django 2.1.4 on 2019-02-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='password',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='police',
            name='username',
            field=models.CharField(default=False, max_length=20),
        ),
    ]