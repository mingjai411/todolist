from django.urls import path
from todolist.views import todoView

urlpatterns = [
    path('todo/', todoView),
]
