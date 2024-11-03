from rest_framework import serializers
from .models import Template


class TemplateSerializer(serializers.ModelSerializer):
    """Serializer for the Template model, including fields for the name, image link, and description"""

    class Meta:
        model = Template
        fields = ["id", "name", "description", "image_link"]
