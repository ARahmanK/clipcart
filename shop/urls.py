from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop),
    path('product/<int:myid>', views.product_view),
    path('about', views.about),
    path('contact', views.contact),
]
