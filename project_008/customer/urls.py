from django.conf.urls import url
from customer import views

app_name = 'customer'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r'^customer_login/', views.customer_login, name="customer_login"),
    url(r'^customer_logout/$', views.customer_logout, name="customer_logout"),
    url(r'^secrete/$', views.secrete_message, name = "secrete"),
]

