# Generated by Django 5.0.2 on 2024-03-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0012_alter_userdeposits_action_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdeposits',
            name='reject',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]