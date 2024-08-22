# Generated by Django 5.0.6 on 2024-07-27 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_batch'),
        ('student', '0005_studentcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.batch')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
