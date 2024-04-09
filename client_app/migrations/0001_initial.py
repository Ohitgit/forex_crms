# Generated by Django 5.0.2 on 2024-04-09 16:11

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
            name='Internal_Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('transfer_from', models.TextField(blank=True, db_index=True, null=True)),
                ('transfer_to', models.TextField(blank=True, db_index=True, null=True)),
                ('amount', models.TextField(blank=True, db_index=True, null=True)),
                ('transaction_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('ip_address', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
            name='Usdt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('usdt', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, null=True)),
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
                ('gender', models.CharField(db_index=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('live_account_limit', models.IntegerField(blank=True, db_index=True, null=True)),
                ('demo_account_limit', models.IntegerField(blank=True, db_index=True, null=True)),
                ('address', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('user_wallet', models.FloatField(blank=True, db_index=True, null=True)),
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
                ('group_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('leverage', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('main_password', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('invest_password', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('phone_password', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
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
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserDeposits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.TextField(blank=True, db_index=True, null=True)),
                ('client_id', models.BigIntegerField(blank=True, db_index=True, default=0, null=True)),
                ('transaction_ID', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('recipet', models.FileField(blank=True, db_index=True, null=True, upload_to='user_upload_document')),
                ('ip_address', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('amount', models.FloatField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('action_choice', models.CharField(choices=[('wallet', 'Wallet'), ('live', 'Live')], db_index=True, default=0)),
                ('deposit_choice', models.CharField(choices=[('usdt', 'USDT'), ('btc', 'BTC'), ('bank', 'BANK')], db_index=True, default='bank')),
                ('usdt_address', models.CharField(blank=True, db_index=True, max_length=120, null=True)),
                ('deposit_from', models.TextField(blank=True, db_index=True, null=True)),
                ('comment', models.TextField(blank=True, db_index=True, null=True)),
                ('reject', models.TextField(blank=True, db_index=True, null=True)),
                ('reference_no', models.CharField(blank=True, db_index=True, max_length=120, null=True)),
                ('status', models.BooleanField(db_index=True, default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
