from django.db import models
from transliterate import translit
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    '''Класс описывающее продукцию'''
    name = models.CharField(max_length=150, verbose_name='Наименование')
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
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')


    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        '''Класс мета-настроек'''
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Blog(models.Model):
    '''Класс описывающий публикуемые статьи в разделе блог'''
    name = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    creation_at = models.DateField(verbose_name='Дата публикации')
    publication = models.BooleanField(default=True, verbose_name='Признак публикации')
    number_views = models.IntegerField(default=0, verbose_name='Количество просмотров')


    def __str__(self):
        return f'{self.name}'

    def delete(self, *args, **kwargs):
        """Удаляет неактивные статьи в Blog """
        self.publication = False
        self.save()


    def get_absolute_url(self):
        """Slug"""
        return reverse('blog_item', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        """Перевод с RU/ENG c заполнением сохранением поля SLUG
        используется бибилиотека transliterate, slugify
        """
        if not self.slug:
            transliterated_name = translit(self.name, 'ru', reversed=True)
            self.slug = slugify(transliterated_name, allow_unicode=True)
        super().save(*args, **kwargs)








    class Meta:
        '''Класс мета-настроек'''
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('name',)