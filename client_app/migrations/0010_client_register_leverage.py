# Generated by Django 5.0.2 on 2024-04-29 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0009_otp_status_status'),
        ('dashboard_app', '0002_forex_manager_credential'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_register',
            name='leverage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard_app.add_leverage'),
        ),
    ]
