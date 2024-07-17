# Generated by Django 5.0.6 on 2024-07-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_notice_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('img', models.ImageField(blank=True, upload_to='event/')),
                ('description', models.TextField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]