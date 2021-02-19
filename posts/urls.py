from django.contrib import admin
from django.urls import Path

urlpatterns = [
    path('', PostListView.as_view(), name='home')
]