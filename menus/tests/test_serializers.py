from rest_framework.test import APITestCase

from menus.models import Template
from menus.serializers import TemplateSerializer


class TemplateSerializerTests(APITestCase):
    def test_template_serialization(self):
        """Test that the serializer correctly serializes template data."""
        template = Template(
            image_link="http://example.com/image.jpg",
            name="Serialized Template",
            description="Template for serialization testing",
        )
        serializer = TemplateSerializer(template)

        # Check if serialized data matches model data
        expected_data = {
            "id": template.id,
            "image_link": "http://example.com/image.jpg",
            "name": "Serialized Template",
            "description": "Template for serialization testing",
        }
        self.assertEqual(serializer.data, expected_data)

    def test_template_deserialization(self):
        """Test that the serializer correctly deserializes template data."""
        data = {
            "image_link": "http://example.com/image.jpg",
            "name": "New Template",
            "description": "Description for new template",
        }
        serializer = TemplateSerializer(data=data)

        # Check if data is valid
        self.assertTrue(serializer.is_valid())
        template = serializer.save()

        # Check if the saved model data matches input data
        self.assertEqual(template.name, data["name"])
        self.assertEqual(template.description, data["description"])
        self.assertEqual(template.image_link, data["image_link"])
