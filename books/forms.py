__author__ = 'User'
from django import forms
from books.models import Section, Catalog, BookLend


class NewBook(forms.ModelForm):
    class Meta(object):
        model = Catalog
        fields = '__all__'


class NewSection(forms.ModelForm):
    class Meta(object):
        model = Section
        fields = '__all__'


class NewBookLend(forms.ModelForm):
    class Meta(object):
        model = BookLend
        fields = '__all__'