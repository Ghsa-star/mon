from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ------------------------------------------------------------
# تحميل ملف البيئة .env
# ------------------------------------------------------------
load_dotenv()

# ------------------------------------------------------------
# المسارات العامة
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------------------------------------------------
# مفاتيح الأمان
# ------------------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = ['mon-z64j.onrender.com', '127.0.0.1', 'localhost']


# ------------------------------------------------------------
# التطبيقات
# ------------------------------------------------------------
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'accounts_profiles',
    'consultations',
    'payments_plans',

    # تطبيقات Cloudinary
    'cloudinary',
    'cloudinary_storage',
]


# ------------------------------------------------------------
# الـ Middleware
# ------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ------------------------------------------------------------
# روابط المشروع
# ------------------------------------------------------------
ROOT_URLCONF = 'mno.urls'


# ------------------------------------------------------------
# إعدادات القوالب (Templates)
# ------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ------------------------------------------------------------
# إعدادات WSGI
# ------------------------------------------------------------
WSGI_APPLICATION = 'mno.wsgi.application'


# ------------------------------------------------------------
# قاعدة البيانات (تطوير + إنتاج)
# ------------------------------------------------------------
if DEBUG:
    # 🧪 قاعدة بيانات التطوير (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # 🚀 قاعدة بيانات الإنتاج (PostgreSQL)
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("DB_ENGINE"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
        }
    }


# ------------------------------------------------------------
# إعدادات كلمات المرور
# ------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ------------------------------------------------------------
# اللغة والمنطقة الزمنية
# ------------------------------------------------------------
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True


# ------------------------------------------------------------
# الملفات الثابتة (Static Files)
# ------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"


# ------------------------------------------------------------
# إعداد Cloudinary (رفع الصور إلى السحابة)
# ------------------------------------------------------------
cloudinary.config( 
    cloud_name = os.getenv("CLOUD_NAME"),
    api_key = os.getenv("CLOUD_API_KEY"),
    api_secret = os.getenv("CLOUD_API_SECRET"),
    secure = True
)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# ------------------------------------------------------------
# إعدادات عامة
# ------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
