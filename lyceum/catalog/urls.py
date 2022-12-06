from catalog import views
from django.urls import path, re_path

app_name = 'catalog'
urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    re_path(r'(?P<pk>[1-9]\d*)/$', views.ItemDetailView.as_view(),
            name='item_detail'),
]
