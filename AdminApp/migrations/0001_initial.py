# Generated by Django 3.2.4 on 2021-07-24 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('artist', models.CharField(max_length=20)),
                ('movie', models.CharField(max_length=20)),
                ('imageurl', models.ImageField(upload_to='images')),
                ('audio_file', models.FileField(upload_to='')),
                ('duration', models.CharField(max_length=20)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.category')),
            ],
            options={
                'db_table': 'Song',
            },
        ),
    ]
