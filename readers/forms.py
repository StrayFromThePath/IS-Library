__author__ = 'User'
from django import forms
from readers.models import Student, Staff, OnceOnly

class NewStudent(forms.ModelForm):
    class Meta(object):
        model = Student
        fields = '__all__'

class NewStaff(forms.ModelForm):
    class Meta(object):
        model = Staff
        fields = '__all__'

class NewOnceOnly(forms.ModelForm):
    class Meta(object):
        model = OnceOnly
        fields = '__all__'