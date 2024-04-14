from django.urls import path

from .views import (
    StockListView, 
    StockDetailView, 
    StockCreateView, 
    StockUpdateView,
    StockDeleteView,
    add_stock_movements,
    
    StockMovementListView,
    StockMovementDetailView,
    StockMovementCreateView,
    StockMovementUpdateView,
    StockMovementDeleteView,
    
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    
    MovementDetailView,
    MovementListView,
    assessment_view
)
urlpatterns = [
    path('stocks/', StockListView.as_view(), name='stock_list'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('stocks/create/', StockCreateView.as_view(), name='stock_create'),
    path('stocks/<int:pk>/update/', StockUpdateView.as_view(), name='stock_update'),
    path('stocks/<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),
    path('stocks/add-movement/<int:pk>', add_stock_movements, name='add_movement'), 
    
    path('stockmovements/<int:pk>', StockMovementListView.as_view(), name='stockmovement_list'),
    path('stockmovements/<int:pk>/', StockMovementDetailView.as_view(), name='stockmovement_detail'),
    path('stockmovements/create/', StockMovementCreateView.as_view(), name='stockmovement_create'),
    path('stockmovements/<int:pk>/update/', StockMovementUpdateView.as_view(), name='stockmovement_update'),
    path('stockmovements/<int:pk>/delete/', StockMovementDeleteView.as_view(), name='stockmovement_delete'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    
    path('assessment/', MovementListView.as_view(), name='assessment_list'),
    path('assessment/<int:pk>/', MovementDetailView.as_view(), name='assessment_detail'),
    path('assessment/movement/<int:pk>/', assessment_view, name='assess_movement'),
]

