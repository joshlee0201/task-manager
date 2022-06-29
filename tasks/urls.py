from django.urls import path

from tasks.views import (
    TaskCreateView,
    Task,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
)


urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
    path("<int:pk>/complete/", TaskUpdateView.as_view(), name="complete_task"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task"),
]
