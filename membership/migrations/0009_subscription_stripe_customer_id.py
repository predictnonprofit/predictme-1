# Generated by Django 3.1.1 on 2020-09-27 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20200927_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
