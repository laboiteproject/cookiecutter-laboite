# cookiecutter-laboite
Cookiecutter template to create an app for La Boîte
=======

You can use [cookiecutter](https://cookiecutter.readthedocs.io/) to help you
create a minimalist scaffolding for your own app. Cookiecutter must be installed, if not use:

```
pip install cookiecutter
```

Let's create a "message of the day" app that will allow you to specify a
message to display. Start by creating the files using cookiecutter:

```
cookiecutter gh:laboiteproject/cookiecutter-laboite
```

You will get prompted to enter a few names:
- `app_name [lowercase_no_spaces]: motd`
- `app_description: Message of the day app`
- `app_model_name [CamelCaseNoSpaces]: MotD`
- `app_verbose_name [Some verbose name]: Message of the Day`
- `author_name: John Doe`
- `author_email: john@doe.com`


### Edit your model

You can now edit the newly created `motd/laboite/apps/motd/models.py` file (we don't need to
do any "updating", so we can skip the "only update any X minutes" part):

```python
class AppMotD(App):
    motd = models.CharField(_('Message'), blank=True, null=True)

    def _get_data(self):
        return {'data': self.motd}

    class Meta:
        verbose_name = _("Configuration : Message of the Day")
        verbose_name_plural = _("Configurations : Message of the Day")
```

### Add your new app to the settings

Edit the `laboite/settings.py` file, and add your app name to the list of existing `INSTALLED_APPS`:

```python
LABOITE_APPS = [
    ...

    "laboite.apps.alarm",
    "laboite.apps.bikes",
    "laboite.apps.bus",
    "laboite.apps.calendar",
    "laboite.apps.energy",
    "laboite.apps.messages",
    "laboite.apps.metro",
    "laboite.apps.parcel",
    "laboite.apps.tasks",
    "laboite.apps.time",
    "laboite.apps.traffic",
    "laboite.apps.weather",
    "laboite.apps.motd",  ## <---- make sure you add your app name to the list!
]
```

### Add your app urls to laboite.urls

Edit `boite.urls` file and add the path to your app urls in `urlpattern`:

```python:
urlpatterns = [
    ...
    
    url(r"^(?P<boite_pk>\d+)/apps/motd/", include('laboite.apps.motd.urls', namespace="app_motd")), ## <---- here it is!
    url(r"^(?P<boite_pk>\d+)/apps/traffic/", include('laboite.apps.traffic.urls', namespace="app_traffic")),
    url(r"^(?P<boite_pk>\d+)/apps/weather/", include('laboite.apps.weather.urls', namespace="app_weather")),
    url(r'^(?P<api_key>[0-9a-z-]+)/$', json_view, name='json'),
    url(r'^redirect/(?P<api_key>[0-9a-z-]+)/$', login_required(redirect_view), name="redirect"),
]
```

### Create and run your migration

Django needs a migration to know how to update your database. However, it's
usually smart enough to create this migration for you!

```
./manage.py makemigrations laboite.apps.motd
./manage.py migrate
```


### Profit!

You can now go to [the admin](http://127.0.0.1:8000/admin), and add a "motd
app" for your *boite*.

Make sure the message you added is displayed in the json displayed on the
*boite* page:
http://127.0.0.1:8000/boites/1/<your_api_key> (replace `1` with the id of your *boite*)

```
{

    ...
    "laboite.apps.motd": [
        {
            "data": "This is my test message of the day!"
        }
    ],
    ...
}
```
