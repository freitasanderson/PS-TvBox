from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.index_title = 'Code Junior'
admin.site.site_url = '/codejunior/'

urlpatterns = [
    path("codejunior/admin/", admin.site.urls),
    path("codejunior/", include('desafios.urls')),
    path("codejunior/forum/", include('forum.urls')),
    path('summernote/', include('django_summernote.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
