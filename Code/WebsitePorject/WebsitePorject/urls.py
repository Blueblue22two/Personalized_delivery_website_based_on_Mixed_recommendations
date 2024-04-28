"""
URL configuration for WebsitePorject project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('polls.urls')),  # add the polls\urls.py to this route
    path('accounts/', include('accounts.urls')),  # accounts: log in&out ,register
    path('carts/', include('cart.urls')),  # shopping cart: manage products
    path('customers/', include('customers.urls')),  # customers: cart, favorite
    path('merchants/', include('merchants.urls')),  # merchant: manage store
    path('orders/', include('orders.urls')),  # merchant: manage store
    path('store/', include('store.urls')),
    path('products/', include('products.urls')),
    path('recommend/', include('recommendation.urls')),
    path('payment/', include('payment.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    # static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
