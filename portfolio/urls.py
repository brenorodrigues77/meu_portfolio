from django.urls import path
from portfolio.views import home, project, detail_project

urlpatterns = [
    path("", view=home, name="home"),
    path("projects/", view=project, name="project"),
    path("projects/<str:project_id>/",
         view=detail_project, name="detail_project"),
]
