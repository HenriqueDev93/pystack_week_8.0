from django.urls import path
from . import views # do diretório atual, busque o arquivo VIEWS

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
]