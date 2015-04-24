# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

class Reader(models.Model):
    class Meta():
        db_table = 'reader'
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'


    name = models.CharField(max_length=20, verbose_name='Имя')
    secondname = models.CharField(max_length=20, verbose_name='Отчество')
    lastname = models.CharField(max_length=40, verbose_name='Фамилия')
    date_add = models.DateField(verbose_name="Дата записи в библиотеку", default=datetime.now())
    date_del = models.DateField(verbose_name="Дата выбития из библиотеки", blank=True, null=True)
    right_read_rom = models.BooleanField(verbose_name='Право пользоваться читальным залом', default=True)
    right_abonement = models.BooleanField(verbose_name='Правило пользоваться абонементом', default=True)

    def __unicode__(self):
        return self.lastname + " " + self.secondname + " " + self.name

class Student(Reader):
    class Meta():
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    group = models.CharField(max_length=20, verbose_name='Название группы')
    faculty = models.CharField(max_length=50, verbose_name='Факультет')

class Staff(Reader):
    class Meta():
        db_table = 'staff'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    chair = models.CharField(max_length=50, verbose_name='Кафедра')
    degree = models.CharField(max_length=50, verbose_name='Степень, Звание', blank=True, null=True)

class OnceOnly(Reader):
    class Meta():
        db_table = 'onceonly'
        verbose_name = 'Разовый читатель'
        verbose_name_plural = 'Разовые читатели'

    phone = models.CharField(max_length=20, verbose_name='Номер телефона')






