from django.urls import path
from .views import RegisterView, LoginView, UserDeleteView, TaskListCreateView, TaskDetailView
from rest_framework_simplejwt.views import  TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("delete-account/", UserDeleteView.as_view(), name="delete-account"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
