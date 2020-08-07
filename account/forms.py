from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    # add additional forms fields to the existing form model
    email = forms.EmailField()
    
    class Meta:
        # Model is saved to 'model'
        model = User
        # The order in which what feilds are shown and in what order.
        fields = ['username','email','password1','password2',]

# inherits form the modelForm
class UserUpdateForm(forms.ModelForm):
    # add additional forms fields to the existing form model
    email = forms.EmailField()
    
    class Meta:
        # Model is saved to 'model'
        model = User
        # The order in which what feilds are shown and in what order.
        fields = ['username','email',]
        
class ProfileUpdateForm(forms.ModelForm):
    # Used the FileInput widget to hide the image path as it is unnecessary
    # Set required = False to make it non mandatory
    image = forms.ImageField(widget = forms.FileInput, required = False)
    class Meta:
        # Model is saved to 'model'
        model = Profile
        # The order in which what feilds are shown and in what order.
        fields = ['image',]
        

        
        

