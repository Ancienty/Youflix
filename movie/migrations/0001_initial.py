# Generated by Django 5.0.3 on 2024-05-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_title', models.CharField(max_length=100)),
                ('overview', models.TextField(max_length=1000)),
                ('poster_link', models.URLField(blank=True, max_length=250, null=True)),
                ('genre', models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=10)),
                ('runtime', models.IntegerField(default=0)),
                ('star1', models.CharField(max_length=100)),
                ('star2', models.CharField(max_length=100)),
                ('star3', models.CharField(max_length=100)),
                ('released_year', models.IntegerField(default=0)),
                ('gross', models.IntegerField(default=0)),
                ('director', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
