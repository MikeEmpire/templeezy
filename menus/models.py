from django.db import models


class Template(models.Model):
    """A model representing a menu template with details about its name image, and description"""

    image_link = models.CharField(
        max_length=200, help_text="URL to an image that represents the template"
    )
    name = models.CharField(max_length=100, help_text="Name of the template")
    description = models.TextField(help_text="A description of the template")

    def __str__(self):
        """Return the name of the template"""
        return self.name
