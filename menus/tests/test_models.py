from django.test import TestCase
from menus.models import Template


class TemplateModelTest(TestCase):

    def setUp(self):
        self.template = Template.objects.create(
            image_link="http://example.com/image.jpeg",
            name="Sample Template",
            description="This is a sample template description",
        )

    def test_template_creation(self):
        """Test that a template can be created"""
        self.assertEqual(self.template.name, "Sample Template")
        self.assertEqual(
            self.template.description, "This is a sample template description"
        )
        self.assertEqual(self.template.image_link, "http://example.com/image.jpeg")
        self.assertIsInstance(self.template, Template)

    def test_template_str_method(self):
        """Test the __str__ method of the Template Model"""
        self.assertEqual(str(self.template), "Sample Template")
