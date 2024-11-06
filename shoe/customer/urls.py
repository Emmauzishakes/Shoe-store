from django.urls import path
from . import views

app_name = "customer"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('category-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<pk>', views.ProductDetail.as_view(), name="product-detail"),
]
