# Generated by Django 5.0.6 on 2024-06-27 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='society_member',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member_id', models.CharField(blank=True, max_length=225, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('house_number', models.CharField(max_length=225)),
                ('mobile_number', models.CharField(max_length=225, unique=True)),
                ('email', models.EmailField(max_length=225, unique=True)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('otp', models.CharField(default='123456', max_length=10)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
