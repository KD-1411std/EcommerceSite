from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
    path("contact/", views.contact, name="contact"),
    path("productView/", views.productView, name="productView"),

]
