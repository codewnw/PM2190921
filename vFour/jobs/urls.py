from django.conf.urls import url
from . import views

app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.JobList.as_view(), name='all'),
    url(r'^(?P<pk>\d+)/', views.JobDetailView.as_view(), name='job_detail'),
]
