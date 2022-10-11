from django.urls import path
from . import views

# Added two urls to the polls app for routing.
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test')
]
