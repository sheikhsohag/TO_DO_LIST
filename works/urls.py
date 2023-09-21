from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add_task/', views.add_task, name = 'add_task'),
    path('show_task/', views.show_task, name = 'show_task'),
    path('delete_task/<int:id>', views.delete_task, name = 'delete_task'),
    path('edit_task/<int:id>', views.edit_task, name = 'edit_task'),
    path('com_task/<int:id>', views.com_task, name = 'com_task'),
    path('completed/', views.complete, name = 'complete'),
    path('delete_task_com/<int:id>', views.delete_task_com, name = 'delete_task_com'),
]
