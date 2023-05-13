from django.urls import path
from .views import index, add

app_name = 'product catalog'

urlpatterns = [
    path('', index, name='index'),
    path('', add, name='add'),
]