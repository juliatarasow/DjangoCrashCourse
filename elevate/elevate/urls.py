from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')), # alle URLs aus der Datei urls.py im api-Ordner werden hinzugefügt
]
