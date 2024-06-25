from django.urls import path
from .views import home_page, create_task, get_task, delete_task

urlpatterns = [
    path("", home_page, name='home'),
    path("create", create_task, name='new'),
    path("view/<int:pk>/task", get_task, name='view'),
    path("delete/<int:pk>/task", delete_task, name='delete'),
]
