from django.contrib import messages
from django.shortcuts import render, redirect
from main.forms import ProjectForm
from main.models import Experience, Project


def show_main(request):
  context = {
      "name": "Muhammad Syarifudin",
      "npm": "2506657112",
      "study_program": "S1 Ilmu Komputer",
      "bio": (
          "Passionate Computer Science student exploring full-stack web"
          " development and AI."
      ),
  }
  return render(request, "index.html", context)


def show_experience(request):
  context = {
      "name": "Muhammad Syarifudin",
      "experience_list": Experience.objects.all(),
  }
  return render(request, "experience.html", context)


def show_project(request):
  context = {
      "name": "Muhammad Syarifudin",
      "project_list": Project.objects.all(),
  }
  return render(request, "project.html", context)


def create_project(request):
  form = ProjectForm(request.POST or None)
  if request.method == "POST" and form.is_valid():
    form.save()
    messages.success(request, "Proyek baru berhasil ditambahkan!")
    return redirect("main:show_project")

  context = {
      "name": "Muhammad Syarifudin",
      "form": form,
  }
  return render(request, "projects_form.html", context)