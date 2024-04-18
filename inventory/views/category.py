from django.urls import reverse_lazy
from inventory.models import Category
from inventory.forms import CategoryForm
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View

class CategoryListView(ListView):
    model = Category
    template_name = 'category/index.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'category'

class CategoryCreateView(SuccessMessageMixin ,CreateView):
    model = Category
    template_name = 'category/create.html'
    form_class = CategoryForm
    success_message = "Category created successfully"
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(SuccessMessageMixin ,UpdateView):
    model = Category
    template_name = 'category/update.html'
    form_class = CategoryForm
    success_message = "Category updated successfully"
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(View):
    model = Category
    success_url = reverse_lazy('category_list')
