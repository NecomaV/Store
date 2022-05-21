# Generated by Django 4.0.2 on 2022-05-21 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userbase_country_alter_userbase_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='about',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='town_city',
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('postcode', models.CharField(max_length=50, verbose_name='Postcode')),
                ('address_line', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('town_city', models.CharField(max_length=150, verbose_name='Town/City/State')),
                ('delivery_instructions', models.CharField(max_length=255, verbose_name='Delivery Instructions')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]