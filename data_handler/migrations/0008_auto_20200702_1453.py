# Generated by Django 3.0.7 on 2020-07-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0007_datafile_unique_id_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafile',
            name='is_donor_id_selected',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
