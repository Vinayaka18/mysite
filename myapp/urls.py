# yourappname/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view
from .views import index_view
from .views import restricted_view


urlpatterns = [
    path('', login_view, name='login'),
    path('index/', index_view, name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('restricted/', restricted_view, name='restricted_view'),

]
