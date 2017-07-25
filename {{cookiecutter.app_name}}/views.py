# coding: utf-8
from __future__ import unicode_literals
from .models import App{{cookiecutter.app_model_name}}
from boites.views import AppCreateView, AppUpdateView, AppDeleteView


class App{{cookiecutter.app_model_name}}CreateView(AppCreateView):
    model = App{{cookiecutter.app_model_name}}
    fields = ['some_field_name']


class App{{cookiecutter.app_model_name}}UpdateView(AppUpdateView):
    model = App{{cookiecutter.app_model_name}}
    fields = ['some_field_name', 'enabled']


class App{{cookiecutter.app_model_name}}DeleteView(AppDeleteView):
    model = App{{cookiecutter.app_model_name}}
