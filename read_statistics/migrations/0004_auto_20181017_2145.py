# Generated by Django 2.0 on 2018-10-17 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0003_readdetail_date_init'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readdetail',
            old_name='date_init',
            new_name='date_new',
        ),
    ]
