# viper-web

fixed the issue with url.py

```python
from django.conf.urls import url
```

This has been depreciated and should now be re_path which uses regex like url.

### example re_path
```python
from django.urls import include, re_path

from myapp.views import home

urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^myapp/', include('myapp.urls'),
]
```

or it can also be path, this does not use regex so you would need to update your URL patterns.

### example path

```python
from django.urls import include, path

from myapp.views import home

urlpatterns = [
    path('', home, name='home'),
    path('myapp/', include('myapp.urls'),
]
```
