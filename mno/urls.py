from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات الخاصة بالمشروع
    path('accounts/', include('accounts_profiles.urls')),   # الحسابات والملفات
    path('consultations/', include('consultations.urls')),  # الاستشارات والمتابعات
    path('payments/', include('payments_plans.urls')),      # الدفع والخطط
]
