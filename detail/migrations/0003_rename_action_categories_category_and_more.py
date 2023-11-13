# Generated by Django 4.2.4 on 2023-11-13 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0002_alter_movie_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='Action',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='Comedy',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='Documentry',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='Drama',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='Mystery',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='Sports',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='War',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='advanture',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='animated',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='horror',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='scifi',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='thriller',
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='detail.categories'),
        ),
    ]