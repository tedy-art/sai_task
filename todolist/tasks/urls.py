from django.urls import path
from .views import dashboard, create_task, update_task, delete_task, user_profile, register, user_login, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', dashboard, name='dashboard'),
    path('create/', create_task, name='create_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('profile/', user_profile, name='user_profile'),
]
