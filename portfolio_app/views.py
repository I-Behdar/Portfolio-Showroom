from django.shortcuts import render
from django.views import View

from portfolio_app.models import Project


class ProjectView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {'projects': projects}
        return render(request, "portfolio_app/display.html", context)

    def post(self, request):
        return render(request, "portfolio_app/display.html")
