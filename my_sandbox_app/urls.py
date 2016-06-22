from django.conf.urls import url
from my_sandbox_app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^place_create/$', views.PlaceCreate.as_view(), name='place_create'),
    url(r'^place_create_done/$', views.place_create_done, name='place_create_done'),
    url(r'^resident_create/$', views.resident_create, name='resident_create'),
    url(r'^resident_create_done/$', views.resident_create_done, name='resident_create_done'),
    url(r"^resident_update/(?P<resident_id>\d+)/$", views.resident_update, name="resident_update"),
]
