from django.urls import path

from . import views

urlpatterns = [path('add_item/<int:id>', views.add_item, name='add_item'),
               path('register', views.add_user, name='register'), path('item/<int:id>', views.item, name='item'),
               path('', views.home, name='all_items'),
               path('items_with_specific_cat/<str:name>', views.all_items, name='cats_items')]
