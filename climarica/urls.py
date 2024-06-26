from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.news_details, name='news_details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('reports/', views.reports, name='reports'),

    path('weather/', views.weather, name='weather'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
