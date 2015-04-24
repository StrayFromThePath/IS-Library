# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from readers.models import Reader, Staff, Student, OnceOnly
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from readers.forms import NewStudent, NewOnceOnly, NewStaff
from django.core.paginator import Paginator
# from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin



def readers_all(request, page_number=1):
    args = {}
    args['staffs'] = Staff.objects.all().order_by('lastname')
    args['onceonly'] = OnceOnly.objects.all().order_by('lastname')
    all_students = Student.objects.all().order_by('lastname')
    current_page = Paginator(all_students, 10)
    args['students'] = current_page.page(page_number)
    return render_to_response('readers_all.html', args)


# Create Student
class CreateStudent(CreateView):
    form_class = NewStudent
    template_name = 'create_student.html'
    success_url = reverse_lazy('all-readers')


# Update Student
class UpdateStudent(UpdateView):
    model = Student
    template_name = 'update_student.html'
    fields = '__all__'
    success_url = reverse_lazy('all-readers')


# Delete Student
class DeleteStudent(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('all-readers')

# Create Staff
class CreateStaff(CreateView):
    form_class = NewStaff
    template_name = 'create_staff.html'
    success_url = '/'


# Update Staff
class UpdateStaff(UpdateView):
    model = Staff
    template_name = 'update_staff.html'
    fields = '__all__'
    success_url = reverse_lazy('all-readers')


# Delete Staff
class DeleteStaff(DeleteView):
    model = Staff
    template_name = 'staff_confirm_delete.html'
    success_url = reverse_lazy('all-readers')


# Create OnceOnly reader
class CreateOnceOnly(CreateView):
    form_class = NewOnceOnly
    template_name = 'create_once.html'
    success_url = reverse_lazy('all-readers')


# Update OnceOnly reader
class UpdateOnceOnly(UpdateView):
    model = OnceOnly
    template_name = 'update_once.html'
    fields = '__all__'
    success_url = reverse_lazy('all-readers')


# Delete OnceOnly reader
class DeleteOnceOnly(DeleteView):
    model = OnceOnly
    template_name = 'once_confirm_delete.html'
    success_url = reverse_lazy('all-readers')