from django.urls import path

from portfolio_app.views import ProjectView

urlpatterns = [
    path("", ProjectView.as_view(), name="project_showroom"),
]
