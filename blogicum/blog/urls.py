
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    # path('posts/<int:pk>/', views.PostListView.as_view(), name='post'),
    path(
        'posts/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts')]
