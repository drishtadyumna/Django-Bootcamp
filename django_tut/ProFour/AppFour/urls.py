from django.conf.urls import include, url
from AppFour import views

urlpatterns = [
    url(r'users', views.user_page, name='user_page'),
    url(r"", views.home_page, name='home_page')
    ]
