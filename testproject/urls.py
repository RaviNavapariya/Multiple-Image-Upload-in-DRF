from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/',views.DetailAPIView.as_view(),name='detail'),
    # path('image-detail/',views.ImageAPIView.as_view(), name='image')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)