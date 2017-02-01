from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class App{{cookiecutter.app_model_name}}Config(AppConfig):
    name = label = 'laboite.apps.{{cookiecutter.app_name}}'
    verbose_name = _('App : {{cookiecutter.app_verbose_name}}')
