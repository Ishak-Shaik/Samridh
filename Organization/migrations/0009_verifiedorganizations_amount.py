# Generated by Django 5.0.3 on 2024-04-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0008_alter_organizationprofile_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifiedorganizations',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
