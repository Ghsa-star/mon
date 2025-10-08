from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
=======
    path("register/", views.register_view, name="register"),  # إنشاء حساب جديد
    path("login/", views.login_view, name="login"),            # تسجيل الدخول
    path("logout/", views.logout_view, name="logout"),          # تسجيل الخروج
>>>>>>> stable
]
