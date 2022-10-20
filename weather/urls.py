from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('info', views.info, name='info'),
    path('about', views.about, name='about')
]
