
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from.import views
urlpatterns = [
    path('',views.index,name="shop"),
    path('about/',views.about,name="about"),
    path('tracker/',views.tracker,name="tracker"),
    path('search/',views.search,name="search"),
    path('contact/',views.contact,name="contact"),
    #path('product/',views.product,name="product"),
    path('checkout/',views.checkout,name="checkout"),
    path("products<int:id>", views.products, name="Product"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path('quickview/<int:product_id>/', views.quick_view, name='quick_view'),
]