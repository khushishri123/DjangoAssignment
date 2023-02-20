from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('save', views.save,name='save'),
    path('update/<int:id>',views.update,name='update'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')
]
