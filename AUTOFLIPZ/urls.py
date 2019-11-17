from django.contrib import admin
from django.urls import path
from users import views as user_views
from management import views as manage_views
from django.contrib.auth import views as auth_views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',manage_views.index,name='home'),
    path('register/', user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('updateProfile/',user_views.update,name='updateProfile'),
    path('profile/',user_views.profile,name='profile')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)