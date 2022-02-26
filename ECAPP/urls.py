
from django.urls import path

from ECAPP import views

urlpatterns = [
    path('',views.home,name="home"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('payfor/',views.payfor,name="payfor"),
    path('contactus/',views.contactus,name="contactus"),
    

]
