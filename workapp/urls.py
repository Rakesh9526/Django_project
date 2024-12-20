from django.urls import path
from . import views

urlpatterns=[
    path('',views.loginn,name='loginn'),
    path('logout',views.loginn,name='logout'),
    # path('signup',views.signup,name='signup'),
    path('index',views.index,name='index'),
    path('apply',views.apply,name='apply'),
    path('user',views.user,name='user'),
    path('newcustomer',views.newcustomer,name='newcustomer'),
    path('searchuser',views.apply,name='searchuser'),
    path('fuelcharge',views.fuelcharge,name='fuelcharge'),
    path('foodallowance',views.foodallowance,name='foodallowance'),
    path('itempurchased',views.itempurchased,name='itempurchased'),
    path('vendorinfo',views.vendorinfo,name='vendorinfo'),
    path('currentstatus',views.currentstatus,name='currentstatus'),
    # path('service',views.newservice,name='service'),
    path('updatefuelcharge/<int:fuel_id>/',views.updatefuelcharge,name='updatefuelcharge'),
    path('updatefoodallowance/<int:food_id>/',views.updatefoodallowance,name='updatefoodallowance'),
    path('updateitempurchased/<int:item_id>/',views.updateitempurchased,name='updateitempurchased'),
    path('updatevendorinfo/<int:vendor_id>/',views.updatevendorinfo,name='updatevendorinfo'),
    path('updatecurrentstatus/<int:status_id>/',views.updatecurrentstatus,name='updatecurrentstatus'),
    
]