# Generated by Django 5.0.6 on 2024-05-31 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]