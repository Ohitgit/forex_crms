# Generated by Django 5.0.2 on 2024-04-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0003_alter_usdt_usdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddocument',
            name='img',
            field=models.FileField(blank=True, db_index=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='uploaddocument',
            name='img2',
            field=models.FileField(blank=True, db_index=True, null=True, upload_to='img2/'),
        ),
    ]
