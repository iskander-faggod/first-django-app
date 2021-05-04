from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Информация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория',
                                 related_name='get_news')
    views = models.IntegerField(default=0)

    def my_func(self):
        return "Hello from model"

    def get_absolute_url(self):
        return reverse_lazy('views_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
