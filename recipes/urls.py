from django.urls import path
from recipes.views import home


urlpatterns = [
    path('', home),  # 127.0.0.1:8000/home/

]
