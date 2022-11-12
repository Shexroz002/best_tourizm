# Generated by Django 4.1.2 on 2022-11-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_etnikturizmrasmlari_extremalturizmrasmlari_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='safarturizmrasmlari',
            name='date',
        ),
        migrations.RemoveField(
            model_name='safarturizmrasmlari',
            name='name_eng',
        ),
        migrations.RemoveField(
            model_name='safarturizmrasmlari',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='safarturizmrasmlari',
            name='name_uzb',
        ),
        migrations.RemoveField(
            model_name='safarturizmrasmlari',
            name='title_eng',
        ),
        migrations.RemoveField(
            model_name='safarturizmrasmlari',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='safarturizmrasmlari',
            name='title_uzb',
        ),
        migrations.AddField(
            model_name='safarturizmrasmlari',
            name='name',
            field=models.CharField(default='images', max_length=90, verbose_name='Rasm nomi'),
        ),
        migrations.AlterField(
            model_name='safarturizmrasmlari',
            name='image_file',
            field=models.ImageField(upload_to='etnik_turizm_rasmlari/', verbose_name='Rasm filesni'),
        ),
        migrations.CreateModel(
            name='SafarTurizmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uzb', models.CharField(default='', max_length=90, verbose_name="Etnik turizm O'zbekcha nomi")),
                ('name_ru', models.CharField(default='', max_length=90, verbose_name='Etnik turizm Ruscha nomi')),
                ('name_eng', models.CharField(default='', max_length=90, verbose_name='Etnik turizm Inglizcha nomi')),
                ('title_uzb', models.TextField(default='', max_length=2500, verbose_name='Etnik turizm haqida malimot kirting(Uzb)')),
                ('title_ru', models.TextField(default='', max_length=2500, verbose_name='Etnik turizm haqida malimot kirting(Rus)')),
                ('title_eng', models.TextField(default='', max_length=2500, verbose_name='Etnik turizm haqida malimot kirting(Eng)')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image_file', models.ManyToManyField(related_name='Etnik', to='api.safarturizmrasmlari', verbose_name='Etnik turizm rasmni kirting')),
            ],
        ),
    ]