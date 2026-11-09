from django.urls import path
from main.views import (
    # Main & Auth
    show_main,
    register,
    login_user,
    logout_user,
    # Experience
    show_experience,
    create_experience,
    create_experience_ajax,
    update_experience,
    delete_experience,
    get_experience_json,
    toggle_star_experience,
    # Projects
    show_project,
    create_project,
    create_project_ajax,
    delete_project,
    get_projects_json,
    toggle_star,
    # Contacts (Tutorial 06 HTMX)
    contact_list,
    contact_add,
    contact_search,
    contact_delete,
    contact_edit,
    contact_row,
    contact_update,
    get_items_json, 
    add_item_ajax,
)

app_name = "main"

urlpatterns = [
    # Halaman Utama
    path("", show_main, name="show_main"),
    
    # Experience URLs
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    
    # Projects URLs
    path("projects/", show_project, name="show_project"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    
    # Auth URLs
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    
    # Contacts HTMX URLs (Tutorial 06)
    path("contacts/", contact_list, name="contact_list"),
    path("contacts/add/", contact_add, name="contact_add"),
    path("contacts/search/", contact_search, name="contact_search"),
    path("contacts/<int:pk>/delete/", contact_delete, name="contact_delete"),
    path("contacts/<int:pk>/edit/", contact_edit, name="contact_edit"),
    path("contacts/<int:pk>/row/", contact_row, name="contact_row"),
    path("contacts/<int:pk>/update/", contact_update, name="contact_update"),
    path('get-items/', get_items_json, name='get_items_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
]