# Generated by Django 5.0.2 on 2024-03-24 07:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0002_rename_userdocument_userdocuments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('documenttype', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('identitytype', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('img', models.FileField(db_index=True, null=True, upload_to='img/')),
                ('img2', models.FileField(db_index=True, null=True, upload_to='img2/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='UserDocuments',
        ),
    ]
