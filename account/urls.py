from django.urls import path
from .views import sing_up_user, login_user, logout_user, edit_user, delete_user, user_profile

urlpatterns = [
    path('sing-up-user/', sing_up_user),
    path('login-user/', login_user),
    path('log-out-user/', logout_user),
    path('edit-user/<int:pk>/', edit_user),
    path('delete-user/<int:pk>/', delete_user),
    path('user-profile/<int:pk>/', user_profile),
]
