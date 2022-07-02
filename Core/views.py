

from lib2to3.pgen2 import token
from operator import imod
from django.shortcuts import redirect, render
from django.views import View
from .forms import SignupForm
from .models import Profile
from django.core.mail import send_mail
import uuid
from django.conf import settings
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import*


# Create your views here.

# Account verification

def account_verify(request,token):
    pf = Profile.objects.filter(token=token).first()
    pf.verify = True
    pf.save()
    messages.success(request,'Your account has been verified ,you can sign-in now')
    return redirect('/signup/')   

class Home(View):
    def get(self,request):
        return render(request,'Core/home.html') 

def send_email_after_registration(email,token):
    subject = 'Verify Email'
    message = f'Hi, Click on the link to verify your account http://127.0.0.1:8000/account-verify/{token}'
    from_email= settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
    

#Signup view    

class SignupView(View):
    def get(self,request):
        form =SignupForm()
        return render(request,'Core/signup.html', context={'title':'Sign Up','form':form})
    def post(self,request):
        form =SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            uid = uuid.uuid4()
            profile_object = Profile(user = new_user,token = uid)
            profile_object.save()
            send_email_after_registration(new_user.email, uid)
            messages.success(request,'Your Account Created Successfully ,to Verify Your Account check your Email')
            return redirect('/signup/')

    
class SignInView(View):
    def get(self,request):
        form =SignInForm()
        return render(request,'Core/sign-in.html',context={'title':'Sign-In','form':form}) 
    def post(self,request):
        form = SignInForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            pro = Profile.objects.get(user = user)
            if pro.verify:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Your account is not verified, please check your Email to verify your account')
                return redirect('/sign-in/')
                
            