from django.urls import path

from .views.templates.list_view import TemplateListView

urlpatterns = [path("templates/", TemplateListView.as_view(), name="Template List")]
