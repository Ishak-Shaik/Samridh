# Generated by Django 5.0.3 on 2024-04-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0005_donations_organization_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='organization_type',
            field=models.CharField(default='Orphanage', max_length=50),
        ),
    ]