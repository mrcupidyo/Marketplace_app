
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('item/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('communication/', include('communication.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:signin'), name='logout'),
]
