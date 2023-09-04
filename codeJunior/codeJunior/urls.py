from django.contrib import admin
from django.urls import include, path

import problemasProgramacao

urlpatterns = [
    path("admin/", admin.site.urls),
    path("problemas/", include('problemasProgramacao.urls'))
]
