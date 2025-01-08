# Generated by Django 5.1.4 on 2025-01-08 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderboardEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('score', models.IntegerField()),
                ('game_type', models.CharField(max_length=100)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
