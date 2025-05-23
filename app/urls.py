from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cars.views import cars_view, new_car_view

urlpatterns = [
                  path("", cars_view, name="cars_list"),
                  path("new_car", new_car_view, name="new_car"),
                  path("admin/", admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
