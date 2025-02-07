# Generated by Django 5.1.5 on 2025-01-28 20:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=250)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creators', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_topic', to='blogs.topic', verbose_name='Topics')),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='blogs_post_created_026960_idx')],
            },
        ),
    ]
