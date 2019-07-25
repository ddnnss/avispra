from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('createform', views.createForm, name='createform'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<cat_name_slug>', views.portfolio_cat, name='portfolio_cat'),
    path('portfolio/<cat_name_slug>/<item_name>', views.portfolio_item, name='portfolio_item'),
    path('contacts/', views.contacts, name='contacts'),
    path('services/', views.services, name='services'),
    path('robots.txt', views.robots, name='robots'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('index.html', views.index, name='index.html'),
    path('index.php', views.index, name='index.php'),
    path('changeInfo/', views.changeInfo, name='getInfo'),



]
