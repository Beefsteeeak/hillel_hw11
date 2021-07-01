from django.urls import path  # noqa:F401

from . import views  # noqa:F401

app_name = 'bookstore'
urlpatterns = [
    path('', views.index, name='index'),
    path('author/', views.author, name='author'),
    path('author/<int:pk>', views.author_detail, name='author-detail'),
    path('publisher/', views.publisher, name='publisher'),
    path('publisher/<int:pk>', views.publisher_detail, name='publisher-detail'),
    path('book/', views.book, name='book'),
    path('book/<int:pk>', views.book_detail, name='book-detail'),
    path('store/', views.store, name='store'),
    path('store/<int:pk>', views.store_detail, name='store-detail'),
]
