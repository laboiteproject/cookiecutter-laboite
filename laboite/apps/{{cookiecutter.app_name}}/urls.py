from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import App{{cookiecutter.app_model_name}}CreateView, App{{cookiecutter.app_model_name}}UpdateView, App{{cookiecutter.app_model_name}}DeleteView


urlpatterns = [
    url(r"^create/$", login_required(App{{cookiecutter.app_model_name}}CreateView.as_view()), name="create"),
    url(r"^(?P<pk>\d+)/$", login_required(App{{cookiecutter.app_model_name}}UpdateView.as_view()), name="update"),
    url(r"^(?P<pk>\d+)/delete/$", login_required(App{{cookiecutter.app_model_name}}DeleteView.as_view()), name="delete"),
]
