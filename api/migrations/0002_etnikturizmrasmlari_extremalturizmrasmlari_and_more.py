# Generated by Django 4.1.2 on 2022-11-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtnikTurizmRasmlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='images', max_length=90, verbose_name='Rasm nomi')),
                ('image_file', models.ImageField(upload_to='etnik_turizm_rasmlari/', verbose_name='Rasm filesni')),
            ],
        ),
        migrations.CreateModel(
            name='ExtremalTurizmRasmlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='images', max_length=90, verbose_name='Rasm nomi')),
                ('image_file', models.ImageField(upload_to='exteremal_turizm_rasmlari/', verbose_name='Rasm filesni')),
            ],
        ),
        migrations.CreateModel(
            name='ExtremalTurizmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uzb', models.CharField(default='', max_length=90, verbose_name="Extremal turizm O'zbekcha nomi")),
                ('name_ru', models.CharField(default='', max_length=90, verbose_name='Extremal turizm Ruscha nomi')),
                ('name_eng', models.CharField(default='', max_length=90, verbose_name='Extremal turizm Inglizcha nomi')),
                ('title_uzb', models.TextField(default='', max_length=2500, verbose_name='Extremal turizm haqida malimot kirting(Uzb)')),
                ('title_ru', models.TextField(default='', max_length=2500, verbose_name='Extremal turizm haqida malimot kirting(Rus)')),
                ('title_eng', models.TextField(default='', max_length=2500, verbose_name='Extremal turizm haqida malimot kirting(Eng)')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image_file', models.ManyToManyField(related_name='imagefile', to='api.extremalturizmrasmlari', verbose_name='exteremal turizm rasmni kirting')),
            ],
        ),
        migrations.CreateModel(
            name='EtnikTurizmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uzb', models.CharField(default='', max_length=90, verbose_name="Etnik turizm O'zbekcha nomi")),
                ('name_ru', models.CharField(default='', max_length=90, verbose_name='Etnik turizm Ruscha nomi')),
                ('name_eng', models.CharField(default='', max_length=90, verbose_name='Etnik turizm Inglizcha nomi')),
                ('title_uzb', models.TextField(default='', max_length=2500, verbose_name='Etnik turizm haqida malimot kirting(Uzb)')),
                ('title_ru', models.TextField(default='', max_length=2500, verbose_name='Etnik turizm haqida malimot kirting(Rus)')),
                ('title_eng', models.TextField(default='', max_length=2500, verbose_name='Etnik turizm haqida malimot kirting(Eng)')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image_file', models.ManyToManyField(related_name='Etnik', to='api.etnikturizmrasmlari', verbose_name='Etnik turizm rasmni kirting')),
            ],
        ),
    ]
