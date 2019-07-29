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
    path('changeHeader/', views.changeHeader, name='changeHeader'),
    path('saveSEO/', views.saveSEO, name='saveSEO'),
    path('changeImg/', views.changeImg, name='changeImg'),
    path('addImg/', views.addImg, name='addImg'),
    path('delImg/', views.delImg, name='delImg'),
    path('saveServiceInfo/', views.saveServiceInfo, name='saveServiceInfo'),
    path('deleteService/', views.deleteService, name='deleteService'),
    path('create_update_category/', views.create_update_category, name='create_update_category'),
    path('createItem/', views.createItem, name='createItem'),
    path('changeItemImg/', views.changeItemImg, name='changeItemImg'),
    path('updateItem/', views.updateItem, name='updateItem'),
    path('deleteItem/', views.deleteItem, name='deleteItem'),
    path('deleteItemImg/', views.deleteItemImg, name='deleteItemImg'),





]
