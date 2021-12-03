from. import views
from django.urls import path

urlpatterns=[
    path('register',views.register,name='demo'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]