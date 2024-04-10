# Generated by Django 5.0.2 on 2024-04-10 15:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forex_Manager_Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('ip', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('login', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
