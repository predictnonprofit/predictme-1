# Generated by Django 3.0.6 on 2020-05-13 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermembership',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermembership',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.Membership'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user_membership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.UserMembership'),
        ),
    ]
