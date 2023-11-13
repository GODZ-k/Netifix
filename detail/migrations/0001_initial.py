# Generated by Django 4.2.4 on 2023-11-13 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scifi', models.CharField(max_length=100)),
                ('horror', models.CharField(max_length=100)),
                ('thriller', models.CharField(max_length=100)),
                ('advanture', models.CharField(max_length=100)),
                ('animated', models.CharField(max_length=100)),
                ('Action', models.CharField(max_length=100)),
                ('Drama', models.CharField(max_length=100)),
                ('Comedy', models.CharField(max_length=100)),
                ('Mystery', models.CharField(max_length=100)),
                ('Documentry', models.CharField(max_length=100)),
                ('War', models.CharField(max_length=100)),
                ('Sports', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('imdb_rating', models.FloatField()),
                ('movie_duration', models.CharField(max_length=20)),
                ('movie_year', models.IntegerField()),
                ('movie_trailler', models.CharField(max_length=200)),
                ('movie_match', models.CharField(max_length=100)),
                ('movie_grade', models.CharField(max_length=200)),
                ('poster_portrait', models.ImageField(upload_to='movie_media')),
                ('director', models.CharField(max_length=200)),
                ('distibuted_by', models.CharField(max_length=200)),
                ('cast', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('quality', models.CharField(max_length=200)),
                ('screenshot_1', models.ImageField(upload_to='movie_media')),
                ('screenshot_2', models.ImageField(upload_to='movie_media')),
                ('screenshot_3', models.ImageField(upload_to='movie_media')),
                ('screenshot_4', models.ImageField(upload_to='movie_media')),
                ('screenshot_5', models.ImageField(upload_to='movie_media')),
                ('screenshot_6', models.ImageField(upload_to='movie_media')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=300)),
                ('released_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='detail.categories')),
            ],
        ),
        migrations.CreateModel(
            name='trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_landscape', models.ImageField(upload_to='movie_media')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trending_movies', to='detail.movie')),
            ],
        ),
        migrations.CreateModel(
            name='poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_wallpaper', models.ImageField(upload_to='movie_media')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster_movies', to='detail.movie')),
            ],
        ),
        migrations.CreateModel(
            name='hot_thrills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=200)),
                ('clip', models.FileField(upload_to='movie_media')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hot_thrills_movies', to='detail.movie')),
            ],
        ),
    ]
