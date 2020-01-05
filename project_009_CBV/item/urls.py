from django.conf.urls import url
from item import views

app_name = 'item'

urlpatterns = [
    url(r'^index/', views.IndexView.as_view(), name='index'),
    url(r'^about_us/', views.AboutUsView.as_view(), name='about_us'),
    url(r'^contact_us/', views.ContactUsView.as_view(), name='contact_us'),
    url(r'^list/', views.ItemListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/', views.ItemDetailView.as_view(), name='detail'),
    url(r'^create/', views.CreateItemView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/', views.UpdateItemView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/', views.DeleteItemView.as_view(), name='delete'),
]
