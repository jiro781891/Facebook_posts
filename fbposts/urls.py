from django.urls import path

from . import views

urlpatterns = [
    path('', views.fetch_post,  name='fetch_post'),

]
