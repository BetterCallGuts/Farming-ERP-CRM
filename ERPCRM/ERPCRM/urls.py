from django.contrib import admin
from django.urls import path, include
from erp_framework.sites import erp_admin_site

urlpatterns = [
    # path('', erp_admin_site.urls),
    path('admin/', admin.site.urls),
    path('', include("core.urls"))
]


