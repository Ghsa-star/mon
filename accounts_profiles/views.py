from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AccountProfile

# عرض نموذج إنشاء حساب
def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if AccountProfile.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم من قبل.")
        else:
            AccountProfile.objects.create(name=name, email=email)
            messages.success(request, "تم إنشاء الحساب بنجاح.")
            return redirect('login')

    return render(request, 'accounts_profiles/register.html')


# عرض نموذج تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = AccountProfile.objects.get(email=email)
            messages.success(request, f"مرحباً {user.name}!")
            return redirect('home')  # تقدر تعدل الوجهة لاحقاً
        except AccountProfile.DoesNotExist:
            messages.error(request, "البريد الإلكتروني غير مسجل.")

    return render(request, 'accounts_profiles/login.html')
