# Generated by Django 5.0 on 2024-07-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Mobile',
            field=models.CharField(max_length=10),
        ),
    ]