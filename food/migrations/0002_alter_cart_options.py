# Generated by Django 4.0.4 on 2022-04-29 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'default_permissions': ('view',)},
        ),
    ]
