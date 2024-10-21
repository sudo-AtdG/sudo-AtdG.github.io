from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_index, name='news_index'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
]
