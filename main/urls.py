from django.urls import path
from main.views import (
    create_experience,
    create_project,
    delete_experience,
    delete_project,
    get_experience_json,
    get_projects_json,
    show_experience,
    show_main,
    show_project,
    update_experience,
    login_user, 
    logout_user, 
    register,
    toggle_star,
    toggle_star_experience,
    create_project_ajax,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    # Experience URLs
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/",update_experience,name="update_experience",),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience",),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    # Projects URLs
    path("projects/", show_project, name="show_project"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project",),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("experience/<uuid:experience_id>/star/",toggle_star_experience,name="toggle_star_experience",),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("experience/add-ajax/",create_experience_ajax,name="create_experience_ajax",),
]
