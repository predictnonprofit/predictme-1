# Generated by Django 3.0.7 on 2020-06-26 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_member_member_ip_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='member_ip_address',
            new_name='ip_address',
        ),
    ]
