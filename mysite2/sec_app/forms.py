from django import forms
from django.contrib.auth.models import User
from sec_app.models import Movement, UserProfileInfo
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

class mat_mov(forms.ModelForm):
    class Meta():
        model = Movement
        fields = '__all__'