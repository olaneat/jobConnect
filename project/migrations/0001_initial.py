# Generated by Django 3.0.8 on 2020-07-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidDetail', models.TextField()),
                ('milestones', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Bid',
                'verbose_name_plural': 'Bids',
                'ordering': ('-user',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('budget', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('job_location', models.CharField(blank=True, max_length=255, null=True)),
                ('bid_deadline', models.DateField(blank=True, null=True)),
                ('skill_required', models.TextField()),
                ('created', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Project Detail',
                'verbose_name_plural': 'Project Details',
            },
        ),
    ]