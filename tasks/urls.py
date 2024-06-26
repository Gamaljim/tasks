from django.urls import path
from .views import home_page, create_task, get_task, delete_task, create_sub_task, get_sub_task, delete_sub_task

urlpatterns = [
    path("", home_page, name='home'),
    path("create", create_task, name='new'),
    path("view/<int:pk>/task", get_task, name='view'),
    path("delete/<int:pk>/task", delete_task, name='delete'),
    path("create_subtask", create_sub_task, name='new_sub_task'),
    path("view/<int:pk>/subtask", get_sub_task, name='view_sub_task'),
    path("delete/<int:pk>/subtask", delete_sub_task, name='delete_sub_task'),



]
