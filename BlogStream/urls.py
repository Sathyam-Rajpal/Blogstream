"""BlogStream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account import views as account_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #homepage
    path('',include('blog.urls')),
    path('admin/', admin.site.urls),
    path('signup/',include('account.urls')),
    path('profile/',account_views.profile,name='profile'),
    
    #default djangoviews login, logout, password so we are not creating a separate view in views.py
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    
    # The password reset page
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name='password_reset'),
    # The default page that tells to see your inbox
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
     # Django automatically looks for template password_reset_confirm to do further work
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    # The password reset complete route, final route
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

]

# We add the media urls to be shown as image in DEBUG mode like this, for production there is a different method
if settings.DEBUG:
    urlpatterns+=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
