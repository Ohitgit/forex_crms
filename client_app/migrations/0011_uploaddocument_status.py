# Generated by Django 5.0.2 on 2024-05-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0010_client_register_leverage'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaddocument',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
