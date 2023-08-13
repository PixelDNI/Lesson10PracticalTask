
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from appTinder.views import display_all_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_all_users),
    path('', include('appTinder.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)