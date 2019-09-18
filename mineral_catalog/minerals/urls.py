from django.urls import path

from minerals import views


urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('<int:pk>/', views.mineral_detail, name='detail'),
]
