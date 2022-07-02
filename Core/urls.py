from django.conf.urls import url
from django.urls import reverse_lazy
from django.urls import path
from .views import Home,SignupView,account_verify,SignInView



app_name ='Core'

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('account-verify/<slug:token>', account_verify, name='account_verify' ),
    path('sign-in/',SignInView.as_view(),name='sign-in'),
  
    
]