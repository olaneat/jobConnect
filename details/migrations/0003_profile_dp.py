# Generated by Django 3.0.8 on 2020-07-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dp',
            field=models.URLField(blank=True, null=True),
        ),
    ]