from django.urls import path, include
from myapp import api

urlpatterns = [
    path('login/', api.userLogin),
    path('userInfo/', api.userInfo),

]
