from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from inventory.models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'category/index.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category/update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(View):
    model = Category
    success_url = reverse_lazy('category_list')
