from django.conf.urls import url
from . import views

app_name = 'web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'execute$', views.execute, name='execute'),
]