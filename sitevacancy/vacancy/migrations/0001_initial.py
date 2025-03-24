# Generated by Django 5.1.7 on 2025-03-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('text', models.TextField(max_length=1000, verbose_name='Описание')),
                ('salary', models.IntegerField(blank=True, verbose_name='Зарплата')),
                ('link', models.URLField(max_length=1000, verbose_name='Ссылка на вакансию на сайте по поиску работы')),
                ('company', models.CharField(max_length=255, verbose_name='Компания')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-create_time'],
                'indexes': [models.Index(fields=['-create_time'], name='vacancy_vac_create__1dc640_idx')],
            },
        ),
    ]
