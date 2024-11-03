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

    def test_template_list_view(self):
        """Test retrieving a list of templates."""
        response = self.client.get(self.url)
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)

        # Check if response data matches serializer data
        self.assertEqual(response.data, serializer.data)
        # Check if response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
