from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView)
from .models import Task, Equipment, FieldGroup, Line, Part
from .forms import TaskForm, EquipmentForm, WorkOrderForm, PartForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'frontend/login.html', {'form': True})  # Pass form error info if needed
    else:
        return render(request, 'frontend/login.html')

class InventoryView(LoginRequiredMixin, View):
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


class DashboardView(LoginRequiredMixin, TemplateView):
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

def add_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontend/part_list')
    else:
        form = PartForm()
    return render(request, 'frontend/add_part.html', {'form': form})


def part_list(request):
    part_list = Part.objects.all()  # Get all parts
    paginator = Paginator(part_list, 50)  # Show 50 parts per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    parts = paginator.get_page(page_number)  # Get the parts for the current page

    return render(request, 'frontend/part_list.html', {'parts': parts})  # Use the correct template path

def search_parts(request):
    query = request.GET.get('q')  # Get the search query
    part_list = Part.objects.all()  # Get all parts

    if query:
        part_list = part_list.filter(
            Q(description__icontains=query) |
            Q(part_number__icontains=query) |
            Q(alt_part_number__icontains=query)
        )

    # Set up pagination
    paginator = Paginator(part_list, 50)  # Show 50 parts per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    parts = paginator.get_page(page_number)  # Get the parts for the current page

    return render(request, 'frontend/part_list.html', {'parts': parts, 'query': query})  # Use the correct template path