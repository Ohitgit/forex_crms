# Generated by Django 5.0.2 on 2024-03-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0009_alter_client_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_register',
            name='gender',
            field=models.CharField(db_index=True, max_length=50, null=True),
        ),
    ]
