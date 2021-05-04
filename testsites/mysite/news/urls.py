from django.urls import path

from news.views import *

urlpatterns = [
    # path('', index, name='home'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('', HomeNews.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('categories/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='views_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]
