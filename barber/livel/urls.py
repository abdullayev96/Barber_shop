from django.urls import path
from .views import *




urlpatterns = [
    path('', home_page, name='home'),
    path('shop/', magazine, name = 'shop'),
    # path('contact/', contact, name = 'contact'),
    # path('about/', about, name = 'about'),
    # path('addpage/', addpage, name='add_page'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]