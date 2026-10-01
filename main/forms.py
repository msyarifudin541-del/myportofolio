from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, Textarea, TextInput, URLInput
from django.utils.html import strip_tags
from main.models import Experience, Project


class ProjectForm(ModelForm):

  class Meta:
    model = Project
    fields = [
        "title",
        "description",
        "tech_stack",
        "project_url",
        "project_image_url",
    ]
    labels = {
        "title": "Nama Proyek",
        "description": "Deskripsi Proyek",
        "tech_stack": "Teknologi yang Digunakan",
        "project_url": "URL Proyek",
        "project_image_url": "URL Gambar Proyek",
    }
    widgets = {
        "title": TextInput(
            attrs={"placeholder": "Portfolio Website", "maxlength": 255}
        ),
        "description": Textarea(
            attrs={"placeholder": "Ceritakan Proyekmu", "rows": 3}
        ),
        "tech_stack": TextInput(
            attrs={"placeholder": "Django, Python, HTML, CSS"}
        ),
        "project_url": URLInput(attrs={"placeholder": "https://github.com/..."}),
        "project_image_url": URLInput(
            attrs={"placeholder": "https://drive.google.com/thumbnail?id=..."}
        ),
    }

  def clean_title(self):
    title = strip_tags(self.cleaned_data["title"]).strip()
    if not title:
      raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
    return title

  def clean_tech_stack(self):
    return strip_tags(self.cleaned_data["tech_stack"]).strip()

  def clean_description(self):
    return strip_tags(self.cleaned_data["description"]).strip()


class ExperienceForm(ModelForm):

  class Meta:
    model = Experience
    fields = [
        "title",
        "description",
        "category",
        "thumbnail",
        "ended_at",
    ]
    labels = {
        "title": "Judul Pengalaman",
        "description": "Deskripsi",
        "category": "Kategori",
        "thumbnail": "URL Gambar Thumbnail",
        "ended_at": "Tanggal Selesai (Kosongkan jika masih berlangsung)",
    }
    widgets = {
        "title": TextInput(
            attrs={"placeholder": "Software Engineering Intern"}
        ),
        "description": Textarea(
            attrs={
                "placeholder": "Jelaskan peran dan pencapaianmu...",
                "rows": 3,
            }
        ),
        "category": Select(attrs={"class": "form-control"}),
        "thumbnail": URLInput(attrs={"placeholder": "https://..."}),
        "ended_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
    }

  def clean_title(self):
    title = strip_tags(self.cleaned_data["title"]).strip()
    if not title:
      raise ValidationError(
          "Judul pengalaman tidak boleh hanya berisi tag HTML."
      )
    return title

  def clean_description(self):
    return strip_tags(self.cleaned_data["description"]).strip()