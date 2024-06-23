# Generated by Django 5.0.6 on 2024-06-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_create_at_employee_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]