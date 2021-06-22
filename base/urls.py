from django.urls import path
from . import views
from . views import TaskList, TaskView, TaskCreate, TaskUpdate, TaskDelete
urlpatterns = [
    path('', TaskList.as_view(), name='home'),
    path('task/<int:pk>/', TaskView.as_view(), name='detail'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('register/', views.register, name='register'),
]


