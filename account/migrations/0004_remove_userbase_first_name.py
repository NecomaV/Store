# Generated by Django 4.0.2 on 2022-05-21 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_userbase_about_remove_userbase_address_line_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='first_name',
        ),
    ]