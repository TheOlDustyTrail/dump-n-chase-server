# Generated by Django 4.1.3 on 2023-01-04 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JerseyPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=1000)),
                ('year', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('bio', models.CharField(max_length=3000)),
                ('logo', models.CharField(max_length=3000)),
                ('carousel1', models.CharField(max_length=3000)),
                ('carousel2', models.CharField(max_length=3000)),
                ('carousel3', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jersey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chaseapi.jerseypost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jerseypost',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chaseapi.team'),
        ),
        migrations.AddField(
            model_name='jerseypost',
            name='user_likes',
            field=models.ManyToManyField(through='chaseapi.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DumpUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('jersey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chaseapi.jerseypost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
