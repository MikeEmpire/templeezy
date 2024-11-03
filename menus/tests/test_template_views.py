from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from menus.models import Template
from menus.serializers import TemplateSerializer


class TemplateViewTest(APITestCase):
    def setUp(self):
        self.template = Template.objects.create(
            image_link="http://example.com/image.jpeg",
            name="Sample Template",
            description="This is a sample template description",
        )
        self.template2 = Template.objects.create(
            image_link="http://example.com/image2.jpg",
            name="Sample Template 2",
            description="Description for Sample Template 2",
        )
        self.url = reverse("template-list")
        self.detail_url = reverse("template-detail", kwargs={"pk": self.template.id})

    def test_template_list_view(self):
        """Test retrieving a list of templates."""
        response = self.client.get(self.url)
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)

        # Check if response data matches serializer data
        self.assertEqual(response.data, serializer.data)
        # Check if response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_template_view(self):
        """Test creating a template"""
        data = {
            "name": "New Template",
            "description": "Description for New Template",
            "image_link": "http://example.com/new_image.jpg",
        }
        response = self.client.post(self.url, data)

        # Check if response status is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if the template was created in the database
        self.assertTrue(Template.objects.filter(name="New Template").exists())

    def test_update_template_view(self):
        """Test updating a template"""
        data = {
            "name": "Updated Template",
            "description": "Updated description",
            "image_link": "http://example.com/updated_image.jpg",
        }
        response = self.client.put(self.detail_url, data)

        # Check if response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the template was updated in the database
        self.template.refresh_from_db()
        self.assertEqual(self.template.name, "Updated Template")
        self.assertEqual(self.template.description, "Updated description")
        self.assertEqual(
            self.template.image_link, "http://example.com/updated_image.jpg"
        )

    def test_delete_template_view(self):
        """Test deleting a template"""
        response = self.client.delete(self.detail_url)

        # Check if response status is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Check if the template was deleted from the database
        self.assertFalse(Template.objects.filter(pk=self.template.id).exists())
