from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView   # <-- أضف هذا

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات الخاصة بالمشروع
    path('accounts/', include('accounts_profiles.urls')),   # الحسابات والملفات
    path('consultations/', include('consultations.urls')),  # الاستشارات والمتابعات
    path('payments/', include('payments_plans.urls')),      # الدفع والخطط

    # الصفحة الرئيسية
    path('', TemplateView.as_view(template_name="home.html"), name='home'),  # <-- هذا السطر المهم
]

# إضافة مسارات الملفات الثابتة والميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
