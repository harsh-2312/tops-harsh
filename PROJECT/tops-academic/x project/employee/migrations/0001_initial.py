# Generated by Django 5.0.6 on 2024-05-31 04:36

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
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('employee_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('otp', models.CharField(default='123456', max_length=10)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]