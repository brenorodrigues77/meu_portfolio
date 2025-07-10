from django.urls import path
from portfolio.views import home, detail_project

urlpatterns = [
    path("", view=home, name="home"),
    path("/<str:project_id>",
         view=detail_project, name="detail_project"),
]
