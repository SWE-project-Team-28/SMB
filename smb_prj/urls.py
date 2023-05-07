from django.contrib import admin
from django.urls import path, include
from smb_users import views as user_view
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('smb_base.urls')),
    path('ckeditor',include('ckeditor_uploader.urls')),
    # Authentication System
    path('register/', user_view.register, name="register"),
    path('login/', auth_view.LoginView.as_view(template_name="smb_users/login.html"), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name="smb_users/logout.html"), name='logout'),
    
    path('profile/', user_view.profile, name="profile"),
    path('profile/update/', user_view.profile_update, name="profile_update"),
    path('profile/questions/', user_view.asked_by_user, name="question_user") 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

