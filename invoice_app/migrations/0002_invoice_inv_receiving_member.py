# Generated by Django 3.0.6 on 2020-05-27 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice_app', '0001_initial'),
        ('membership', '0002_auto_20200527_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='inv_receiving_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.UserMembership'),
        ),
    ]
