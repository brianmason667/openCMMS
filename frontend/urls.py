# urls.py

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-confirm-delete'),
    path('', DashboardView.as_view(), name='home'),
    path('equipment/', EquipmentListView.as_view(), name='equipment-list'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/create/', views.EquipmentCreateView.as_view(), name='equipment-create'),
    path('fieldgroups/', FieldGroupListView.as_view(), name='fieldgroup-list'),
    path('work-orders/', WorkOrdersView.as_view(), name='work-orders'),
    path('asset-management/', AssetManagementView.as_view(), name='asset-management'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('scheduling/', SchedulingView.as_view(), name='scheduling'),
    path('user-management/', UserManagementView.as_view(), name='user-management'),
    path('work-order/create/', work_order_create, name='work-order-create'),
]
