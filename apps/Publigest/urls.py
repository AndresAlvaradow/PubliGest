from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.contrib import admin
app_name = 'Publigest'
urlpatterns = [
    path('login/',LoginView.as_view(template_name ='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name ='login.html'), name='logout'),
    path('main/', views.main, name='index'),
    path('graf/', views.grafic, name="grafico"),
    path('tab/', views.extrac, name="tablas"),
    path('ner/', views.entidades, name="entidades"),
    path('nert/', views.entidades_text, name="entidades_text"),
    path('kw/', views.keyWords, name="KeyW"),
    path('admin/', admin.site.urls),

]