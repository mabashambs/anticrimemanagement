# Generated by Django 2.1.4 on 2019-02-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_complent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complent',
            name='complent_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]