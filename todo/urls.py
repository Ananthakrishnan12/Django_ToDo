from django.urls import path
from todo import views

urlpatterns = [
    # Add task
    path('add_task/',views.add_task,name="add_task"),
    # Mark task as Done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name="mark_as_done"),
    # Mark task as Undone
    path('mark_as_Undone/<int:pk>',views.mark_as_Undone,name="mark_as_Undone"),
    # Edit task
    path('edit_task/<int:pk>/',views.edit_task,name="edit_task"),
    # Delete task
    path('delete_task/<int:pk>/',views.delete_task,name="delete_task"),
]