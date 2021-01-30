from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
   path('',views.indexpage,name='index'),
   path('update/<int:id>',views.update),
   path('delete/<int:id>',views.delete),
]
