from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import Template
from ...serializers import TemplateSerializer


class TemplateListView(APIView):
    """View to handle CRUD of templates"""

    @swagger_auto_schema(
        operation_description="Retrieve a list of templates.",
        responses={200: openapi.Response(description="List of Templates")},
    )
    def get(self, request):
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data)

    """ Endpoint to create a template """

    @swagger_auto_schema(
        operation_description="Create a new template.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "description": openapi.Schema(type=openapi.TYPE_STRING),
                "image_link": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            201: openapi.Response(description="New Template Created"),
            400: openapi.Response(
                description="Bad Request - Validation Errors",
                examples={
                    "application/json": {
                        "name": ["This field is required."],
                        "image_link": ["Invalid URL format."],
                    }
                },
            ),
        },
    )
    def post(self, request):
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
