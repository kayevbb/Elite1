# Generated by Django 2.2.8 on 2020-02-28 15:41

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
            name='Pole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Город')),
                ('body', models.TextField(verbose_name='Информация о туре')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Фото')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('avatar3', models.ImageField(upload_to='', verbose_name='Фото')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('status', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.CharField(max_length=255)),
                ('spot', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='el_travel.Pole')),
            ],
        ),
        migrations.CreateModel(
            name='PoleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('pole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='el_travel.Pole')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='el_travel.Pole')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
