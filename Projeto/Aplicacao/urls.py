from django.urls import path
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('adicionar/', views.AddView.as_view(), name="add"),
]