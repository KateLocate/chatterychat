from django.contrib import admin
from django.urls import include, path

import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(auth.urls)),
]
