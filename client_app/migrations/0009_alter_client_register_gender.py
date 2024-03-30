# Generated by Django 5.0.2 on 2024-03-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0008_client_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_register',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], db_index=True, max_length=50, null=True),
        ),
    ]
