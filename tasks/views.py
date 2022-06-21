from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
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
