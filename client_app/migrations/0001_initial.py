# Generated by Django 5.0.2 on 2024-03-24 07:04

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('otp_status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('documenttype', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('identitytype', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('img', models.FileField(db_index=True, null=True, upload_to='img/')),
                ('img2', models.FileField(db_index=True, null=True, upload_to='img2/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('email_status', models.BooleanField(default=False)),
                ('mobile_no', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('dob', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('mobile_status', models.BooleanField(default=False)),
                ('username', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('uuid', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('live_account_limit', models.IntegerField(blank=True, db_index=True, null=True)),
                ('demo_account_limit', models.IntegerField(blank=True, db_index=True, null=True)),
                ('address', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LiveAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('ip', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('login', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('group', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('leverage', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('main_password', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('invest_password', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('phone_password', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
