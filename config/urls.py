"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from uploader.router import router as uploader_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from FedoraCoffee import views
from user.router import router as user_router

router = DefaultRouter()
router.register(r"clients", views.ClientViewSet)
router.register(r"orders", views.OrderViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"products", views.ProductViewSet)
router.register(r"items", views.ItemViewSet)
router.register(r"extras", views.ExtraViewSet)
router.register(r"ordersExtras", views.orderExtraViewSet)
router.register(r"ordersProducts", views.orderProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(user_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/products_by_category/", views.ProductsByCategoryView.as_view())
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)