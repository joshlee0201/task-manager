from django.urls import path

from tasks.views import TaskCreateView, Task


urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="create_task"),
]
