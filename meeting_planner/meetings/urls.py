from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms_list, name="rooms"),
    path('new', views.new, name="new"),
    path('<int:id>/edit', views.edit, name="edit"),
    path('<int:id>/delete', views.delete, name="delete")
]