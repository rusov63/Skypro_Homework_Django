from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    '''Класс описывающее продукцию'''
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    creation_at = models.DateField(verbose_name='Дата создания')
    modified_at = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.category} {self.price} {self.modified_at}'

    class Meta:
        '''Класс мета-настроек'''
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


class Category(models.Model):
    '''Класс описывающее категорию'''
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')


    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        '''Класс мета-настроек'''
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)