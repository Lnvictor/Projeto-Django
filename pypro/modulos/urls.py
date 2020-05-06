from django.urls import path

from pypro.base.views import home
from pypro.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
]
