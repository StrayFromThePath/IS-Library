__author__ = 'User'
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from books.models import Section, Catalog, BookLend
from books.forms import NewBook, NewSection, NewBookLend
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
# from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin
from datetime import datetime


# List book catalog
class ListBookView(ListView):
    model = Catalog
    template_name = 'book__list.html'
    context_object_name = 'books'
    queryset = Catalog.objects.all().order_by('date_reg')


# Create Book
class CreateBook(CreateView):
    form_class = NewBook
    template_name = 'create_book.html'
    success_url = reverse_lazy('book-list')


# Update Book catalog
class UpdateBook(UpdateView):
    model = Catalog
    template_name = 'update_book.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')


# Delete Book
class DeleteBook(DeleteView):
    model = Catalog
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')


# List section
class ListSectionView(ListView):
    model = Section
    template_name = 'section__list.html'
    context_object_name = 'sections'
    queryset = Section.objects.all().order_by('name')


# Create section
class CreateSection(CreateView):
    form_class = NewSection
    template_name = 'create_section.html'
    success_url = reverse_lazy('all-section')


# Update Book catalog
class UpdateSection(UpdateView):
    model = Section
    template_name = 'update_section.html'
    fields = '__all__'
    success_url = reverse_lazy('all-section')


# Delete Section
class DeleteSection(DeleteView):
    model = Section
    template_name = 'section_confirm_delete.html'
    success_url = reverse_lazy('all-section')


class ListBookLendView(ListView):
    model = BookLend
    template_name = 'book-lend__list.html'
    context_object_name = 'books'
    queryset = BookLend.objects.all()


class CreateBookLend(CreateView):
    form_class = NewBookLend
    template_name = 'create_booklend.html'
    success_url = reverse_lazy('book-list')


class UpdateBookLend(UpdateView):
    model = BookLend
    template_name = 'update_booklend.html'
    fields = ['abonement1', 'abonement2', 'read_room', 'lend_date_fact', 'mark_return']
    success_url = reverse_lazy('book-list')

