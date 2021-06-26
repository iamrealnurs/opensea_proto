from django.contrib import admin
from django.urls import path, include
from opensea.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls', 'main'))),
    path('about/', about),
]
