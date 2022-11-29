from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('modify/<int:user_id>', modify, name='modify'),
    path('delete/<int:user_id>', delete, name='delete')
]
