from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('topics-listing/', views.topics_listing, name='topics-listing'),
    path('topics-detail/', views.topics_detail, name='topics-detail'),
    path('buy-coffee/', views.buy_coffee, name='buy-coffee'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('account-center/', views.account_center, name='account-center'),
    path('calculus/', views.calculus, name='calculus'),
    # path('forum/', views.forum, name='forum'),
]
