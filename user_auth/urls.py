from django.urls import path, include
from .views import UserRegisterView, UserEditView, PasswordChangeView, ProfilePageView, EditProfileView, CreateProfileView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('/profile/settings/', UserEditView.as_view(), name='edit_settings'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordChangeView.as_view()),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile', ProfilePageView.as_view(), name="profile"),
    path('/profile/<int:pk>/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('set_up_profile/', CreateProfileView.as_view(), name="create_profile"),
]