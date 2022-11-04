from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    technology = models.CharField(max_length=128)
    image = models.FilePathField(path="/portfolio_app/static/images")

    def __str__(self):
        return f"{self.title}, {self.technology}"

