from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from.views import Profile

urlpatterns = [
    path('api/profile',Profile.as_view(),name='profile'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)