"""DjangoRestFramework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from  Api import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('admin/', admin.site.urls),
    
    # path('products/', views.product_list),
    # path('products/<int:pk>/', views.product_details),
    #  path('orders/', views.order_list),
    #  path('products-info/', views.product_info),
    # path('products/', views.ProductListAPIView.as_view()),
    #  path('products/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('products/<int:product_id>/' , views.ProductDetailAPIView.as_view()),
     path('products/info/', views.ProductInfoAPIView.as_view()),
     path('orders/', views.OrderListAPIView.as_view()),
     path('user-orders/', views.UserOrderListAPIView.as_view(), name='user-orders'),
     path('product/<int:product_id>/' , views.ProductDetailUpdateAPIView.as_view()),

     path('products/create', views.ProductCreateAPIView.as_view()),
    path('products/', views.ProductListCreateAPIView.as_view()),
     path('silk/', include('silk.urls',namespace='silk'))
]
