# Generated by Django 5.0 on 2024-07-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_details_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
