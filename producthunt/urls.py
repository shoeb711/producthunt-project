from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from producthunt.settings import MEDIA_ROOT
from products import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls'))
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
