# Generated by Django 5.0.2 on 2024-04-02 15:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0013_userdeposits_reject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internal_Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('transfer_from', models.TextField(blank=True, db_index=True, null=True)),
                ('amount', models.TextField(blank=True, db_index=True, null=True)),
                ('transaction_ID', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('ip_address', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='liveaccount',
            name='group_name',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
    ]