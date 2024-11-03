from django.urls import path

from .views.templates.detail_view import TemplateDetailView
from .views.templates.list_view import TemplateListView

urlpatterns = [
    path("templates/", TemplateListView.as_view(), name="template-list"),
    path("templates/<int:pk>/", TemplateDetailView.as_view(), name="template-detail"),
]
