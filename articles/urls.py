
from django.urls import path
from django.utils.crypto import get_random_string

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path("create/", views.article_create, name="create"),
    path('birthday/', views.article_birthday, name="birthday"),
    path('anniversary/', views.article_anniversary, name="anniversary"),
    path('getwell/', views.article_getwell, name="getwell"),
    path('sympathy/', views.article_sympathy, name="sympathy"),
    path('graduation/', views.article_graduation, name="graduation"),
    # path('<slug:slug>/', views.article_occasion, name="occasion"),
    path('<slug:slug>/', views.article_detail, name="detail"),
]

