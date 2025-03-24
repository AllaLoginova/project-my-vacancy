# Generated by Django 5.1.7 on 2025-03-21 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='vacancy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='vacancy.vacancy', verbose_name='Вакансия'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.IntegerField(blank=True, null=True, verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='text',
            field=models.TextField(max_length=3000, verbose_name='Описание'),
        ),
    ]
