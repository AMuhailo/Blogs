# Generated by Django 5.1.5 on 2025-01-28 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.PositiveIntegerField()),
                ('content_ct', models.ForeignKey(limit_choices_to={'model__in': ('text', 'image', 'video')}, on_delete=django.db.models.deletion.CASCADE, related_name='content_objects', to='contenttypes.contenttype')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_post', to='blogs.post', verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(upload_to='content/image/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_content', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
                'indexes': [models.Index(fields=['created'], name='blogs_image_created_21af39_idx')],
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_content', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
                'indexes': [models.Index(fields=['created'], name='blogs_text_created_67f282_idx')],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('video', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_content', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
                'indexes': [models.Index(fields=['created'], name='blogs_video_created_7c0d20_idx')],
            },
        ),
    ]
