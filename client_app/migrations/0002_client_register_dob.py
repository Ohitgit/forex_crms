# Generated by Django 5.0.2 on 2024-03-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_register',
            name='dob',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
    ]