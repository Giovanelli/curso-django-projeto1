from django.urls import path

# Quando for importar um arquivo irmão da mesma pasta.
# Significa: da pasta onde eu estou import views.
from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),  # 127.0.0.1:8000/home/
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]

# o parâmetro name no função path é para dar um nome único para URL
