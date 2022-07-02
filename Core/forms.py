
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import password_validation



class SignupForm(UserCreationForm):
    
    # username =forms.CharField(required=True,max_length=15)
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'})
        
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
       
    )
    email =forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username","email")
        
    
    
    
        
        
        
class SignInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(
         label='Password',
         strip=False,
        
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


        
