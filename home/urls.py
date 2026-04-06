from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getyourwebsite/', views.getyourwebsite, name='getyourwebsite'),
    path('aftersubmit/', views.aftersubmit, name='aftersubmit'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('pricing/', views.pricing, name='pricing'),
    path('service/', views.service, name='service'),
    path('workedwith/', views.workedwith, name='workedwith'),
    path('dashbord/', views.dashbord, name='dashbord'),

    path('automotive/', views.automotive),
    path('business/', views.business),
    path('ecommerce/', views.ecommerce),
    path('education/', views.education),
    path('gym/', views.gym),
    path('healthcare/', views.healthcare),
    path('portfolio_example/', views.portfolio_example),
    path('realestate/', views.realestate),
    path('restaurant/', views.restaurant),
    path('saas/', views.saas),
    path('coffee_shop/', views.coffee_shop),
]