from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ...models import Template
from ...serializers import TemplateSerializer


class TemplateListView(APIView):
    """Endpoint to retrieve a list of templates"""

    @swagger_auto_schema(
        method="get",
        operation_description="Retrieve a list of templates.",
        responses={200: openapi.Response(description="List of Templates")},
    )
    def get(self, request):
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data)
