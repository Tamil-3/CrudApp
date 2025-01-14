from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('update/<int:id>', views.update, name="update"),
    path('addrec/', views.addrec, name="addrec"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/updaterec/<int:id>', views.updaterec, name="updaterec"),
]