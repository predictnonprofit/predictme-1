# Generated by Django 3.1.1 on 2020-09-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0011_auto_20200929_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='stripe_card_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
