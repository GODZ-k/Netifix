# Generated by Django 4.2.4 on 2023-11-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hot_thrills',
            name='label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]