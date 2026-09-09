from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Muhammad Syarifudin",
        "npm": "2506657112",
        "study_program": "S1 Ilmu Komputer",
        "bio": "Passionate Computer Science student exploring full-stack web development and AI. Dedicated to building innovative software solutions.",
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Muhammad Syarifudin",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)