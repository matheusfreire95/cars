from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cars.views import CarsListView, CarsDetailView, CarsCreateView, CarsUpdateView, CarsDeleteView
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('', CarsListView.as_view(), name='cars_list'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('new_car/', CarsCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarsDetailView.as_view(), name='detail_car'),
    path('car/<int:pk>/update', CarsUpdateView.as_view(), name='edit_car'),
    path('car/<int:pk>/delete', CarsDeleteView.as_view(), name='delete_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
