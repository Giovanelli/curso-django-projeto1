from django.urls import path
from recipes.views import home, contato, sobre


urlpatterns = [
    path('', home),  # 127.0.0.1:8000/home/
    path('sobre/', sobre),
    path('contato/', contato)
]
