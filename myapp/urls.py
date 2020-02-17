from django.urls import path

from myapp import views

# Add your URL patterns here
urlpatterns = [
    path('ping', views.ping),
]
