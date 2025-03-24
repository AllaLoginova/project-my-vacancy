from django.db import models

class Vacancy(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название вакансии')
    text = models.TextField(max_length=3000, verbose_name='Описание')
    salary = models.IntegerField(blank=True, null=True, verbose_name='Зарплата')
    link = models.URLField(max_length=1000, verbose_name='Ссылка на вакансию на сайте по поиску работы')
    company = models.CharField(max_length=255, verbose_name='Компания')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-create_time']
        indexes = [
            models.Index(fields=['-create_time'])
        ]

class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name='Текст')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, related_name='comments', verbose_name='Вакансия', null=True)
