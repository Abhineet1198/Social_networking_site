
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from .settings import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('profile2/', views.profile2, name='profile2'),
    path('editprofile/', views.editprofile, name='editprofile'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=MEDIA_ROOT)
