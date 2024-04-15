from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("propos",views.propos,name="propos"),
    path("notes",views.vnotes, name="unotes"),
    path("connexion", views.log_, name="login-page"),
    path("inscription", views.sign_, name="signin-page"),
    path("log_out", views.log_out, name="logout"),
    path("add-note",views.add_note),
    path("search",views.search, name="search"),
    path("<str:slug>", views.update_notes),
]
