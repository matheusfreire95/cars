from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cars.views import cars_view, new_car_view
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('', cars_view, name='cars_list'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('new_car/', new_car_view, name='new_car'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
