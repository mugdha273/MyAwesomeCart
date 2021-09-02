from . import views
from django.urls import path

urlpatterns = [
    path("",views.index, name="ShopHome"),
    path('about/', views.about,name="AboutUs"),
    path('tracker', views.tracker,name="TrackingStatus"),
    path('contact/',views.contact, name="Contactus"),
    path('search/', views.search,name="Search"),
    path('productview/', views.productView,name="ProductView"),
    path('checkout/', views.checkout,name="Checkout"),

]
