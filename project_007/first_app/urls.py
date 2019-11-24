from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'registration/', views.registration_view, name="registration_view"),
    url(r'itemform/', views.item_view, name="item_view"),
]
