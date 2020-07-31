from django.urls import path
from . views import todo_list,todo_details,todo_create,todo_update,todo_delete
app_name = "app"

urlpatterns = [
    path('',todo_list),
    path('create/',todo_create),
    path('<int:id>',todo_details),
    path('<int:id>/update',todo_update),
    path('<int:id>/delete',todo_delete),
    
]

