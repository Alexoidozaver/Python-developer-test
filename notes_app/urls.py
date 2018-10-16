from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.post_list, name='post_list'),
    #url('form', views.test_form, name='test_form'),
]