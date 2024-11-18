from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, 
                            blank=False,
                            verbose_name = 'Название')
    description = models.TextField(blank=False, 
                                   verbose_name = 'Описание')
    slug = models.SlugField(blank=False, 
                            verbose_name = 'Идентификатор',
                            help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.')
    is_published = models.BooleanField(blank=False, 
                                        verbose_name = 'Опубликовано',
                                        help_text='Снимите галочку, чтобы скрыть публикацию.')
    created_at = models.DateField(blank=False, 
                                  verbose_name = 'Добавлено')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории' 


class Location(models.Model):
    name = models.CharField(max_length=256, 
                            blank=False, 
                            verbose_name = 'Название места')
    is_published = models.BooleanField(blank=False, 
                                       verbose_name = 'Опубликовано',
                                       help_text='Снимите галочку, чтобы скрыть публикацию.')
    created_at = models.DateField(blank=False, 
                                  verbose_name = 'Добавлено')

    class Meta:
        verbose_name = 'локация'
        verbose_name_plural = 'локации' 


class Post(models.Model):
    title = models.CharField(max_length=256, 
                             blank=False, 
                             verbose_name = 'Заголовок')
    text = models.TextField(blank=False, 
                            verbose_name = 'Текст')
    pub_date = models.DateField(blank=False, 
                                verbose_name = 'Дата и время публикации',
                                help_text='Если установить дату и время в будущем — можно делать отложенные публикации.')
    is_published = models.BooleanField(blank=False, 
                                       verbose_name = 'Опубликовано',
                                       help_text='Снимите галочку, чтобы скрыть публикацию.')
    created_at = models.DateField(blank=False, 
                                  verbose_name = 'Добавлено')
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               blank=False,
                               related_name='posts', 
                               verbose_name = 'Автор публикации')
    location = models.ForeignKey(Location,
                                on_delete=models.SET_NULL, 
                                null=True,
                                blank=True, 
                                related_name='posts', 
                                verbose_name = 'Местоположение')
                 
    category = models.ForeignKey(Category, 
                                on_delete=models.SET_NULL, 
                                null=True,
                                blank=False, 
                                related_name='posts', 
                                verbose_name = 'Категория')
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'посты' 
