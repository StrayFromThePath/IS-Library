__author__ = 'User'
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from readers.models import Reader
import select2
from select2 import fields


class Section(models.Model):
    class Meta():
        db_table = 'section'
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


    name = models.CharField(max_length=255, verbose_name='Название')

    def __unicode__(self):
        return self.name


class Catalog(models.Model):
    class Meta():
        db_table = 'catalog'
        verbose_name = 'Каталог книг'
        verbose_name_plural = 'Каталог книг'


    title = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=255, verbose_name='Автор/Авторы')
    publisher = models.CharField(max_length=100, verbose_name="Изадельство")
    date_publ = models.CharField(max_length=4, verbose_name="Дата издания")
    date_reg = models.DateField(verbose_name="Дата регистрации", auto_now_add=True)
    section = models.ForeignKey(Section, verbose_name="Раздел")
    abonement1 = models.BooleanField(default=False, verbose_name="Абонемент 1")
    abonement2 = models.BooleanField(default=False, verbose_name="Абонемент 2")
    read_room = models.BooleanField(default=False, verbose_name="Читальный зал")
    price = models.DecimalField(verbose_name="Стоимость", max_digits=7, decimal_places=2)
    count_all = models.IntegerField(verbose_name="Общее кол-во")
    count_in = models.IntegerField(verbose_name="Кол-во в наличии")
    count_ab1 = models.IntegerField(verbose_name="Кол-во в Абонементе 1", blank=True, null=True)
    count_ab2 = models.IntegerField(verbose_name="Кол-во в Абонементе 2", blank=True, null=True)
    count_rr = models.IntegerField(verbose_name="Кол-во в Читальном зале", blank=True, null=True)

    def __unicode__(self):
        return self.author + " " + self.title


class BookLend(models.Model):
    class Meta():
        db_table = 'book_lend'
        verbose_name = 'Выдача книги'
        verbose_name_plural = 'Выдача книг'

    reader = select2.fields.ForeignKey(Reader, verbose_name="Читатель", overlay="Выберите читателя",)
    book = select2.fields.ForeignKey(Catalog, verbose_name="Книга")
    abonement1 = models.BooleanField(default=False, verbose_name="Абонемент 1")
    abonement2 = models.BooleanField(default=False, verbose_name="Абонемент 2")
    read_room = models.BooleanField(default=False, verbose_name="Читальный зал")
    lend_date = models.DateField(default=datetime.now, verbose_name="Дата выдачи", editable=False)
    lend_date_end = models.DateField(verbose_name="Дата возврата")
    lend_date_fact = models.DateField(verbose_name="Фактическая дата возврата", null=True, blank=True)
    mark_return = models.BooleanField(default=False, verbose_name="Отметка о возврате")

    def get_absolute_url(self):
        return reverse('booklend-list', kwargs={'pk': self.pk})

    def save(self):
        item = Catalog.objects.get(id=self.book_id)
        if self.abonement1 and self.mark_return == 0:
            item.count_in -= 1
            item.count_ab1 -= 1
            item.save()
        elif self.mark_return and self.abonement1:
            item.count_in += 1
            item.count_ab1 += 1
            item.save()
        elif self.abonement2 and self.mark_return == 0:
            item.count_in -= 1
            item.count_ab2 -= 1
            item.save()
        elif self.abonement2 and self.mark_return:
            item.count_in += 1
            item.count_ab2 += 1
            item.save()
        elif self.read_room and self.mark_return == 0:
            item.count_in -= 1
            item.count_rr -= 1
            item.save()
        elif self.read_room and self.mark_return:
            item.count_in += 1
            item.count_rr += 1
            item.save()
        super(BookLend, self).save()

