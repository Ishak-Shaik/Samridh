# Generated by Django 5.0.3 on 2024-04-09 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0004_unverifiedorganizations_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fields', models.JSONField()),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.verifiedorganizations')),
            ],
        ),
    ]
