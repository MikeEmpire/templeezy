from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import Template
from ...serializers import TemplateSerializer


class TemplateDetailView(APIView):
    """View to handle details of templates, like update, get a single template, or delete a template"""

    """Endpoint to get a single template"""

    @swagger_auto_schema(
        operation_description="Retrieves a single template",
        responses={
            200: openapi.Response(description="Single Template"),
            404: openapi.Response(description="Template Not Found"),
        },
    )
    def get(self, request, pk):
        try:
            template = Template.objects.get(pk=pk)
        except Template.DoesNotExist:
            return Response("Template Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = TemplateSerializer(template)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """ Endpoint to update template """

    @swagger_auto_schema(
        operation_description="Update Template",
        responses={
            404: openapi.Response(description="Template Not Found"),
            400: openapi.Response(
                description="Bad Request - Validation Errors",
                examples={
                    "application/json": {
                        "name": ["This field is required."],
                        "image_link": ["Invalid URL format."],
                    }
                },
            ),
            200: openapi.Response(
                description="Updated Template",
            ),
        },
    )
    def put(self, request, pk):
        try:
            template = Template.objects.get(pk=pk)
        except Template.DoesNotExist:
            return Response("Template Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = TemplateSerializer(template, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """ Endpoint to delete template """

    @swagger_auto_schema(
        operation_description="Delete a template by ID.",
        responses={
            204: openapi.Response(description="Template Deleted"),
            404: openapi.Response(description="Template Not Found"),
        },
    )
    def delete(self, request, pk):
        try:
            template = Template.objects.get(pk=pk)
        except Template.DoesNotExist:
            return Response("Template Not Found", status=status.HTTP_404_NOT_FOUND)
        template.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
