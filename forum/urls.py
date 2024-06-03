from django.conf import settings
from django.conf.urls.static import static
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
    path('calculus/ask/', views.calculus_ask, name='calculus-ask'),
    path('login/', views.login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
