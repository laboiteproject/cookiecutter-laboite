# coding: utf-8

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

from boites.models import App


class App{{cookiecutter.app_model_name}}(App):
    #### TODO: Change UPDATE_INTERVAL if you need to call `update_data` every now and then (eg from a webservice)
    UPDATE_INTERVAL = None

    ##### TODO: List your fields here.
    some_field_name = models.TextField(_(u'Some Field Name'), blank=True, null=True)

    def _get_data(self):
        """This method returns a dict containing the data that will be encoded to JSON"""
        return {'data': self.some_field_name}

    def update_data(self):
        """Retrieve external data (if needed) and store them"""
        ##### TODO: Update the model field here: request some data, use Weboob...
        # response = requests.get("http://example.com")

        ##### TODO: Then store in the model.
        # self.some_field_name = response.text
        # self.save()

    class Meta:
        verbose_name = _('Configuration : {{cookiecutter.app_verbose_name}}')
        verbose_name_plural = _('Configurations : {{cookiecutter.app_verbose_name}}')
