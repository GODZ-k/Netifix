# Generated by Django 4.2.4 on 2023-11-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0006_alter_categories_options_alter_hot_thrills_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hot_thrills',
            name='name_color',
            field=models.CharField(default='grey', max_length=100),
        ),
    ]
