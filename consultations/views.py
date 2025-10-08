from django.shortcuts import render
from .models import Consultation

def home_view(request):
    """
    الصفحة الرئيسية — تعرض أحدث الاستشارات مع صورها.
    """
    # جلب آخر 6 استشارات مرتبة من الأحدث إلى الأقدم
    consultations = Consultation.objects.all().order_by('-id')[:6]

    context = {
        "consultations": consultations,
    }
    return render(request, "home.html", context)
