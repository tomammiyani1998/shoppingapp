from . import views
from django.urls import path
app_name = 'searchapp'

urlpatterns = [
    path('', views.searchapp, name='search_products'),
]