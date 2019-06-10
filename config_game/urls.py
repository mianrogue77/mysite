from django.urls import path

from .views import list_elements, create_element, list_efects, create_efects, update_efects, delete_efects

urlpatterns = [
    path('list', list_elements, name='list_elements'),
    path('new', create_element, name='create_element'),
    path('list_efects', list_efects, name='list_efects'),
    path('new_efects', create_efects, name='create_efects'),
    path('update_efects/<int:id>/', update_efects, name='update_efects'),
    path('delete_efects/<int:id>/', delete_efects, name='delete_efects'),
]