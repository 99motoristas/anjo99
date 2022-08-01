from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('increase_counter/<int:group_id>', views.increase_counter, name='increase_counter'),
]
