from django.urls import path
from . import views

urlpatterns = [
    # Quando o usuário acessar a raiz do site, ele vai chamar a função index da views.py
    path('', views.index, name='index'),

]