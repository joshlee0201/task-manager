from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        return redirect("show_project", pk=task.project.id)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/list.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("show_my_tasks")
