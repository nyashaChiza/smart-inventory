from django.urls import path
from integration.views import (
    IntegrationCreateView,
    IntegrationListView,
    IntegrationDetailView,
    IntegrationDeleteView,
    IntegrationTestConnection,
    IntegrationEnableView,
    IntegrationUpdateView,
)
urlpatterns = [
    path('index', IntegrationListView.as_view(), name='integration-list'),
    path('details/<int:pk>', IntegrationDetailView.as_view(), name='integration-details'),
    path('create/', IntegrationCreateView.as_view(), name='integration-create'),
    path('update/<int:pk>', IntegrationUpdateView.as_view(), name='integration-update'),
    path('delete/<int:pk>', IntegrationDeleteView.as_view(), name='integration-delete'),
    path('integration/test/<int:pk>', IntegrationTestConnection.as_view(), name="integration-test"),
    path('integration/toggle/<int:pk>', IntegrationEnableView.as_view(), name="integration-enable"),
    
]