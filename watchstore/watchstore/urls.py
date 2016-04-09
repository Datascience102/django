"""watchstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from dukaan.views import dukaanam, index, stock, newwatch

# this worked, this should've been done, imported app.views into project views and ran the server
# ok, first import all the views from the app,
# then, add all the urls using just include, for now go on.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dukaan/$', 'dukaan.views.dukaanam'),
    url(r'^index/$',index),
    url(r'^$', 'dukaan.views.index'),
    url(r'^stock/$', 'dukaan.views.stock'),
    url(r'^newitem/$', 'dukaan.views.newwatch'),
    url(r'^accounts/', include('registration.backends.default.urls')),
            ]
