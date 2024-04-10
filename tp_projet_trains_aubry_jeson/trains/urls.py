from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('show/<id_train>', views.show, name="show"),
    path('random', views.random, name="random"),
]

