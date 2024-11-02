from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView)
from .models import Task, Equipment, FieldGroup, Line
from .forms import TaskForm, EquipmentForm, WorkOrderForm

class InventoryView(View):
    def get(self, request):
        return render(request, 'frontend/inventory.html')

class ReportsView(View):
    def get(self, request):
        return render(request, 'frontend/reports.html')

class SchedulingView(View):
    def get(self, request):
        return render(request, 'frontend/scheduling.html')

class UserManagementView(View):
    def get(self, request):
        return render(request, 'frontend/user_management.html')

class AssetManagementView(View):
    def get(self, request):
        return render(request, 'frontend/asset_management.html')

class WorkOrdersView(View):
    def get(self, request):
        return render(request, 'frontend/work_orders.html')
    
def work_order_create(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work-order-list')  # Redirect after saving
    else:
        form = WorkOrderForm()
    return render(request, 'frontend/work_order_form.html', {'form': form})

class DashboardView(TemplateView):
    template_name = 'frontend/dashboard.html'

class TaskListView(ListView):
    """View to list all tasks."""
    model = Task
    template_name = 'frontend/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    """View to display details of a specific task."""
    model = Task
    template_name = 'frontend/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    """View to create a new task."""
    model = Task
    template_name = 'frontend/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    """View to update an existing task."""
    model = Task
    template_name = 'frontend/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    """View to delete a task."""
    model = Task
    template_name = 'frontend/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

class EquipmentListView(ListView):
    """View to list all equipment."""
    model = Equipment
    template_name = 'frontend/equipment_list.html'
    context_object_name = 'equipment_list'

# class EquipmentCreateView(CreateView):

#     model = Equipment
#     fields = ['name', 'description']  # specify form fields
#     template_name = 'app/equipment_form.html'
#     success_url = '/equipment/'  # redirect after successful form submission

class EquipmentCreateView(CreateView):
    model = Equipment
    form_class = EquipmentForm  # Use your custom form
    template_name = 'frontend/equipment_form.html'
    success_url = '/equipment/'  # Redirect after successful form submission

    def get_context_data(self, **kwargs):
        """Add lines to the context for the template."""
        context = super().get_context_data(**kwargs)
        context['lines'] = Line.objects.all()  # Fetch all lines to display in the template
        return context

class EquipmentDetailView(DetailView):
    """View to display details of a specific equipment."""
    model = Equipment
    template_name = 'frontend/equipment_detail.html'
    context_object_name = 'equipment'

class FieldGroupListView(ListView):
    """View to list all field groups."""
    model = FieldGroup
    template_name = 'frontend/fieldgroup_list.html'
    context_object_name = 'fieldgroups'
