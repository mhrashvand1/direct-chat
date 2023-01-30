from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator


User = get_user_model()

class SignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "name")
    
        
class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=150, label=_("Username"), required=True)
    password = forms.CharField(label=_("Password"), strip=False, required=True)        
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError(
                message="Invalid username/password",
                code=400
            )
        else:
            return {**self.cleaned_data, "user":user}
        
  
        
class ProfileForm(forms.Form):
    
    username = forms.CharField(
        max_length=150, label=_("Username"), 
        required=True, 
        validators=[UnicodeUsernameValidator()] ##
    )
    name = forms.CharField(max_length=150, required=True)
    avatar = forms.ImageField(required=False)
    
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance")
        super().__init__(*args, **kwargs)
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists() and not self.instance.username == username:
            raise ValidationError(
                message=f"A user exists with this username: {username}",
                code=400
            )
        return username
       
    def save(self):
        data = self.cleaned_data
        user = self.instance
        profile = user.profile
        if data.get("avatar"):
            profile.avatar = data.get("avatar")
        user.username = data.get("username", user.username)
        user.name = data.get("name", user.name)
        user.save()
        profile.save()
        return user
    
