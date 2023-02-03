from django.urls import path
from .views import *

urlpatterns = [
    path('tag-system/', home_view, name="home"),
    path('post/<slug:slug>/', detail_view, name="detail"),
    path('tag/<slug:slug>/', tagged, name="tagged")
]
