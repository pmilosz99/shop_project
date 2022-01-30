from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('login/refresh/', views.UserRetrieveUpdateAPIView.as_view(), name='login_refresh'),
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
]