# Generated by Django 3.1.1 on 2020-09-27 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0007_remove_usermembership_data_handler_session'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='member',
            new_name='member_id',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='active',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_end_date',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_start_date',
        ),
        migrations.AddField(
            model_name='subscription',
            name='card_brand',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='card_expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='card_last_4_digits',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='stripe_plan_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membership.membership'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_period_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_period_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
