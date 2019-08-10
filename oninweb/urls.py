"""oninweb URL Configuration
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include
import basicapp.views 
import signup.views
import supply.views

from django.urls import path

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view()),
    # url(r'^logout/$', auth_views.logout, name = 'logout'),# builtin
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name = 'logout'),# page redirect
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('', basicapp.views.index),
    path('signup/', signup.views.Signup),
    path('thanks/', signup.views.thanks),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('supply/', include('supply.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
