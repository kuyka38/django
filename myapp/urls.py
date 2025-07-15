
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views. home,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('products/', views.products, name='products'),

    path('login/', views.login_view, name='login'),
   path('', views.register, name='register'),

]
