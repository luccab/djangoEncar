from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('get_name', views.get_name, name='get_name'),
    path('get_data', views.get_data, name='get_data'),
]
