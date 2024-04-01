# Generated by Django 5.0.2 on 2024-03-30 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0011_client_register_user_wallet_userdeposits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdeposits',
            name='action_choice',
            field=models.CharField(choices=[('wallet', 'Wallet'), ('live', 'Live')], db_index=True, default=0),
        ),
    ]