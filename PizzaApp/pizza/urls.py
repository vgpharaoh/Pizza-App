from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('owner/', views.owner, name='owner'),
    path('chef/', views.chef, name='chef'),
    path('addtopping/<str:name>/', views.addtopping, name='addtopping'),
    path('remtopping/<int:name>/', views.remtopping, name='remtopping'),
    path('updtopping/<int:select>/<str:name>/', views.updtopping, name='updtopping'),
    path('addpizza/<str:name>/<str:toppings>', views.addpizza, name='addpizza'),
    path('rempizza/<int:name>/', views.rempizza, name='rempizza'),
    path('updpizza/<int:select>/<str:name>/<str:toppings>/', views.updpizza, name='updpizza'),
]