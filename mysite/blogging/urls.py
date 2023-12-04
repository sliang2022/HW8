from django.urls import path
from blogging.views import list_view, detail_view

urlpatterns = [
    path('posts/', list_view.as_view(), name="blog_index"),
    path('posts/<int:pk>/', detail_view.as_view(), name="blog_detail"),
]
