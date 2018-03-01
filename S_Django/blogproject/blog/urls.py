from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.blog_index),
    path('blog/', views.blog_title),
    path('blog/<article_id>/', views.blog_article)
]