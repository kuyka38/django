
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views. home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('gallery/', views.gallery),
    path('products/', views.products),
]
