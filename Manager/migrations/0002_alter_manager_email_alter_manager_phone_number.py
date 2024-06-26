# Generated by Django 5.0.3 on 2024-04-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
