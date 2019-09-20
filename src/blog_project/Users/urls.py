from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('profile/',views.profile, name='blog_profile'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
]

# static is only debug 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

