from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AccountProfile


def register_view(request):
    """
    إنشاء حساب جديد
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        # التحقق من إدخالات المستخدم
        if not name or not email:
            messages.error(request, "الرجاء إدخال جميع الحقول المطلوبة.")
            return redirect("register")

        # التحقق من وجود البريد مسبقًا
        if AccountProfile.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مسجل مسبقًا.")
            return redirect("register")

        # إنشاء الحساب الجديد
        AccountProfile.objects.create(name=name, email=email)
        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
        return redirect("login")

    return render(request, "accounts_profiles/register.html")


def login_view(request):
    """
    تسجيل الدخول
    """
    if request.method == "POST":
        email = request.POST.get("email")

        # التحقق من البريد الإلكتروني المدخل
        if not email:
            messages.error(request, "يرجى إدخال البريد الإلكتروني.")
            return redirect("login")

        try:
            user = AccountProfile.objects.get(email=email)
            # حفظ اسم المستخدم في الجلسة
            request.session["user_name"] = user.name
            messages.success(request, f"مرحبًا {user.name}!")
            return redirect("home")  # يمكنك تعديل الوجهة لاحقًا
        except AccountProfile.DoesNotExist:
            messages.error(request, "البريد الإلكتروني غير مسجل لدينا.")
            return redirect("login")

    return render(request, "accounts_profiles/login.html")


def logout_view(request):
    """
    تسجيل الخروج
    """
    # مسح بيانات الجلسة للمستخدم
    request.session.flush()
    messages.info(request, "تم تسجيل الخروج بنجاح.")
    return redirect("home")
