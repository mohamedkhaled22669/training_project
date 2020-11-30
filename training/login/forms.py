from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=80)
    password = forms.CharField(max_length=20)
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=80)
    password = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=10)