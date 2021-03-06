# Generated by Django 4.0.4 on 2022-04-29 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import food.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('desc', models.TextField(blank=True, default=None, null=True)),
                ('category', models.CharField(default=None, max_length=225)),
                ('image', models.ImageField(default=None, upload_to=food.models.uploadimage)),
                ('price', models.IntegerField(default=None)),
                ('added_to_cart', models.BooleanField(default=False)),
                ('stock', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=None)),
                ('TotalPrice', models.IntegerField(default=None)),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
