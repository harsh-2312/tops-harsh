# Generated by Django 5.0.6 on 2024-07-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_visitor_entry_time_alter_visitor_exit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='exit_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]