# Generated by Django 5.0.2 on 2024-04-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0004_alter_uploaddocument_img_alter_uploaddocument_img2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdeposits',
            name='usdt_address',
            field=models.CharField(blank=True, db_index=True, max_length=500, null=True),
        ),
    ]
