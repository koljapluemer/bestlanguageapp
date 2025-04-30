from django.urls import path
from app.presenter.admin.tool import list, edit, delete, create

app_name = 'admin.tool'

urlpatterns = [
    path('', list.list_tools, name='list'),
    path('create/', create.handle_create_tool, name='create'),
    path('<int:id>/edit/', edit.edit_tool, name='edit'),
    path('<int:id>/delete/', delete.delete_tool, name='delete'),
]
