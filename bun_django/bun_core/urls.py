from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from bun_core.views import news, about, home, test, create_,delete_

urlpatterns = [
    path("",home,name="home"),
    path("news/", news, name="news"),
    path("about/",about,name="about"),
    path("create/",create_, name="create"),
    path("test/",test,name="test"),
    path('delete/<int:id>',delete_,name="delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)