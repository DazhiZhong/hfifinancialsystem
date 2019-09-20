from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.teamhome_redirect,name='redirect_to_list'),
    path('post/', views.home, name='blog_home'),
    path('features/', views.features, name='blog_features'),
    path('new/', views.new, name='blog_new'),
    path('ab/', views.abbs, name='test001'),
    path('load/', views.load, name='load'),
    path('homepage/<int:teamnum>/', views.teamhome, name='teamhome'),
    path('homepage/', views.teamlist, name='teamlist'),
    path('homepage/', views.teamhome_redirect, name='teamhome_redirect'),
    path('bidding/',views.bidding,name='bidding'),    
    path('bidding_successful/',views.buyall,name='buyall'),
    path('pickle/',views.pickle_my_class,name='pickle'),    
    path('pickle_payload/',views.pickle_payload,name='picklepayload'),
    path('deletepickle',views.delete_pickle,name='deletepickle'),
    path('country/',views.countryv,name='country')
]