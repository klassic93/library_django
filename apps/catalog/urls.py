from django.urls import path
from apps.catalog import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books')
]
