from django.urls import path
from .views import ItemView, ItemDetailView, ItemEdit, ItemDelete,ItemCreateView

urlpatterns = [
    path('item/', ItemView.as_view(), name='list'),
    path('item-create/', ItemCreateView.as_view(), name='create'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('item/<int:pk>/edit', ItemEdit.as_view(), name='edit'),
    path('item/<int:pk>/delete', ItemDelete.as_view(), name='delete'),

]
