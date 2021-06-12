# Generated by Django 2.1.4 on 2019-02-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190223_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.IntegerField(primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
            ],
        ),
    ]
