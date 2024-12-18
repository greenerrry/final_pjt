# Generated by Django 4.2.16 on 2024-11-26 02:27

import datetime
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
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('title', models.CharField(default='untitled', max_length=255)),
                ('release_date', models.DateField()),
                ('poster_path', models.TextField()),
                ('backdrop_path', models.TextField(blank=True, null=True)),
                ('overview', models.TextField()),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('rating', models.CharField(blank=True, max_length=10, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('cast', models.JSONField(default=list)),
                ('genres', models.ManyToManyField(related_name='movies', to='movie.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('timestamp', models.CharField(blank=True, max_length=50, null=True)),
                ('text', models.TextField()),
                ('difficulty_level', models.CharField(choices=[('Beginner', '초급'), ('Intermediate', '중급'), ('Advanced', '고급')], max_length=20)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', to_field='tmdb_id')),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('meaning', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('word', 'category')},
            },
        ),
        migrations.CreateModel(
            name='FavoriteMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_tmdb_id', models.CharField(max_length=50)),
                ('movie_title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DifficultyLevelMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginner', models.IntegerField()),
                ('intermediate', models.IntegerField()),
                ('advanced', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('tmdb_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', to_field='tmdb_id')),
            ],
        ),
        migrations.CreateModel(
            name='UserScriptProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_match_rate', models.IntegerField(default=0)),
                ('highest_points', models.IntegerField(default=0)),
                ('last_attempt', models.DateTimeField(auto_now=True)),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.script')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['user', 'highest_match_rate'], name='movie_users_user_id_289653_idx'), models.Index(fields=['script', 'highest_match_rate'], name='movie_users_script__8caa2b_idx')],
                'unique_together': {('user', 'script')},
            },
        ),
        migrations.CreateModel(
            name='FavoriteWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning_date', models.DateField(default=datetime.datetime(2024, 11, 26, 2, 27, 8, 336586, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_words', to=settings.AUTH_USER_MODEL)),
                ('vocabularyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorited_by', to='movie.vocabularyword')),
            ],
            options={
                'unique_together': {('user', 'vocabularyword')},
            },
        ),
    ]
