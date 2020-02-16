from django.urls import path
from travelling import views

urlpatterns = [
    path('', views.showtravelling, name='home'),
    path('Register/', views.showRegister, name='Register'),
    path('login/', views.showlogin, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('BookNow/', views.bookNow, name='BookNow')

]
