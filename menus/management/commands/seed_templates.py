from django.core.management.base import BaseCommand

from menus.models import Template


class Command(BaseCommand):
    help = "Seeds the database with example template data."

    def handle(self, *args, **kwargs):
        templates_data = [
            {
                "name": "Classic Menu Template",
                "description": "A classic menu template with a customizable text area.",
                "image_link": "https://example.com/classic_menu_background.jpg",
            },
            {
                "name": "Modern Café Template",
                "description": "A clean, modern design suitable for cafes and bistros.",
                "image_link": "https://example.com/modern_cafe_background.jpg",
            },
            {
                "name": "Elegant Dinner Menu",
                "description": "An elegant template ideal for fine dining.",
                "image_link": "https://example.com/elegant_dinner_menu.jpg",
            },
        ]

        for template_data in templates_data:
            template, created = Template.objects.get_or_create(
                name=template_data["name"],
                defaults={
                    "description": template_data["description"],
                    "image_link": template_data["image_link"],
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created template: {template.name}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Template already exists: {template.name}"))

        self.stdout.write(self.style.SUCCESS("Database seeded with example templates."))
